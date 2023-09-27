from json import dumps
from os import getenv
from urllib import parse

from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from fastapi.routing import APIRouter
from oauthlib.oauth2 import WebApplicationClient
from requests import get, post
from sqlmodel import Session, select
from starlette.config import Config

from ....security import create_login_jwt
from ....settings import GOOGLE_OAUTH_CLIENT_ID, GOOGLE_OAUTH_CLIENT_SECRET
from ...db import engine
from ...db.user import User

google = APIRouter(prefix="/google")
oauth = WebApplicationClient(GOOGLE_OAUTH_CLIENT_ID)
oauth_cfg = get("https://accounts.google.com/.well-known/openid-configuration").json()

@google.get('/')
def index(request: Request):
    redirect_uri = str(request.url) + "callback"
    authorization_endpoint = oauth_cfg['authorization_endpoint']

    request_uri = oauth.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=redirect_uri,
        scope=['openid', 'email', 'profile']
    )
    return RedirectResponse(request_uri, 308)

@google.get('/callback', include_in_schema=False)
def callback(request: Request, code: str, scope: str, authuser: str, prompt: str, hd: str):
    token_endpoint = oauth_cfg['token_endpoint']
    token_url, headers, body = oauth.prepare_token_request(
        token_endpoint, 
        redirect_url=str(request.url.remove_query_params(["code", "scope", "authuser", "prompt", "hd"])),
        code=code
    )
    token_response = post(token_url, headers=headers, data=body, auth=(GOOGLE_OAUTH_CLIENT_ID, GOOGLE_OAUTH_CLIENT_SECRET)).json() # type: ignore
    oauth.parse_request_body_response(dumps(token_response))

    userinfo_endpoint = oauth_cfg['userinfo_endpoint']
    uri, headers, body = oauth.add_token(userinfo_endpoint)
    data = get(uri, headers=headers, data=body).json()

    if data.get("email_verified"):
        with Session(engine) as session:
            try:
                user = session.exec(select(User).where(User.email==data['email'])).one()
            except :
                user = User(tag=data['email'], name=data["name"], image=data["picture"], email=data["email"]) # type: ignore
                session.add(user)
                session.commit()
            response = RedirectResponse(str(request.base_url))
            response.set_cookie("x-fastinni-login-jwt", create_login_jwt(user), httponly=True, secure=True)
            return response
            
    else:
        return RedirectResponse(str(request.base_url) + 
            "/error?title=" + parse.quote("Email Not Verified") + 
            "&data=" + parse.quote(f"Your email {data['email']} was not verified by Google. Please try again later.")
        )
        
