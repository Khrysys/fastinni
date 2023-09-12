from fastapi.routing import APIRouter

api = APIRouter()

from .csrf import csrf
api.include_router(csrf, prefix="/csrf")