from datetime import datetime, timedelta
from functools import lru_cache
from json import dumps
from os import getenv

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse
from oauthlib.oauth2 import WebApplicationClient
from requests import get, post
from sqlmodel import Session, SQLModel, select

from ..security import OWaspValidationException, validate_email_address

from .. import User, engine


@lru_cache
def get_google_provider_cfg():
    return get("https://accounts.google.com/.well-known/openid-configuration").json()

client = WebApplicationClient(getenv("GOOGLE_CLIENT_ID"))
app = APIRouter(prefix="/google")

@app.get("/")
def redirect_to_google_login(request: Request):
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    
    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri= str(request.url) + "callback",
        scope=["openid", "email", "profile"]
    )
    
    return RedirectResponse(request_uri)

@app.get("/callback")
def google_login_callback(code: str, request: Request):
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]# Prepare and send a request to get tokens! Yay tokens!
    
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=str(request.url),
        code=code
    )
    token_response = post(
        token_url,
        headers=headers,
        data=body,
        auth=(getenv("GOOGLE_CLIENT_ID"), getenv("GOOGLE_CLIENT_SECRET")), # type: ignore
    )

    # Parse the tokens!
    client.parse_request_body_response(dumps(token_response.json()))
    
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = get(uri, headers=headers, data=body)
    
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400
    
    # Validate the user's email against OWasp requirements, just in case.
    # This doesn't return anything since this will throw an OWaspValidationException if it fails
    # Google has stricter requirements than we do, but this is probably important to keep in here.
    
    # The error handler is in api/exceptions.py
    validate_email_address(users_email)
        

    user = User.try_login_user(email=users_email, google_id=unique_id)

    if user is None:
        with Session(engine) as session:
            # We now know this is a new login to this site
            user = User(display_name=users_name, tag=users_email, email=users_email, google_id=unique_id)
            session.add(user)
            session.commit()

    response = RedirectResponse(request.url.hostname) # type: ignore
    response.set_cookie(getenv("LOGIN_JWT_TOKEN_NAME", 'login'), user.generate_login_jwt())
    return response