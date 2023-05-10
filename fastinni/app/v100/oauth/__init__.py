from fastapi.routing import APIRouter

app = APIRouter(prefix='/oauth')

from . import google

app.include_router(google.app)
