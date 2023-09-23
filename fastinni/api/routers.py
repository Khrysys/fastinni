from fastapi.routing import APIRouter

latest = APIRouter(prefix="/latest", tags=['Latest'])
dev = APIRouter(prefix="/dev", tags=["In Development"])

from .v100 import v100
latest.include_router(v100)
