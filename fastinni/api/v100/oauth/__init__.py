from fastapi.routing import APIRouter
oauth = APIRouter(prefix='/oauth')

from authlib.integrations.starlette_client import OAuth
oauth_app = OAuth()

from .google import google
oauth.include_router(google)
