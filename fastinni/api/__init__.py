from fastapi.routing import APIRouter
from starlette.routing import Route

api = APIRouter(prefix="/api")

from .routers import latest, dev
from . import csrf

api.include_router(latest)
api.include_router(dev)