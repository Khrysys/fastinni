from fastapi.routing import APIRouter
from ..routers import latest

oauth = APIRouter(prefix='/oauth')

from .google import google
oauth.include_router(google)

latest.include_router(oauth)