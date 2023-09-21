from fastapi.routing import APIRouter
from starlette.config import Config
from os import getenv
from fastapi.requests import Request

google = APIRouter(prefix="/google")

from . import oauth_app as oauth

oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=getenv("GOOGLE_OAUTH_CLIENT_ID"),
    client_secret=getenv("GOOGLE_OAUTH_CLIENT_SECRET"),
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@google.get('/')
async def index(request: Request):
    redirect_uri = request.url_for("callback")
    print(redirect_uri)
    return await oauth.google.authorize_redirect(request, redirect_uri)

@google.get('/callback')
async def callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    return token
