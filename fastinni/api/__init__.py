from fastapi.routing import APIRouter
from starlette.routing import Route

api = APIRouter(prefix="/api")

from .routers import latest, dev
api.include_router(latest)
api.include_router(dev)
from .v100 import v100
api.include_router(v100, prefix='/v100', tags=['Version 1.0.0'])