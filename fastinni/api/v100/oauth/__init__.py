from fastapi.routing import APIRouter
oauth = APIRouter(prefix='/oauth')

from .google import google
oauth.include_router(google)
