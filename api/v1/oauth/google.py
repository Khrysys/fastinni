from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse
from oauthlib.oauth2 import WebApplicationClient
from os import getenv
from requests import get
from functools import lru_cache
from json import dumps
from requests import get, post
from sqlmodel import SQLModel, Session, select
from ...db import User, engine

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
def google_callback(code: str):
    return RedirectResponse(f'../../../../?google_code={code}', )
    
@app.get("/finalize")
def finalize_google_login(code: str, request: Request):
    
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
    
    # Find if the user already exists, and if not, add a new user
    with Session(engine) as session:
        statement = select(User).where(User.email==users_email)
        results = session.exec(statement)

        user = results.one_or_none()
        if user is not None:
            
            (data, status) = user.get_own_data()
            response = RedirectResponse('../../../../', status_code=status)