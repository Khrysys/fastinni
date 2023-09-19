from fastapi.routing import APIRouter

v100 = APIRouter()

from .account import account
v100.include_router(account)
from .csrf import csrf
v100.include_router(csrf)
from .data import data
v100.include_router(data)