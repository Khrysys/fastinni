from fastapi.routing import APIRouter

from .v100 import v100

latest = APIRouter(prefix="/latest", tags=['Latest'])
dev = APIRouter(prefix="/dev", tags=["In Development"])

latest.include_router(v100)
