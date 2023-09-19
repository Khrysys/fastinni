from fastapi.routing import APIRouter

v100 = APIRouter()

from .account import account
v100.include_router(account)
from .contact import contact
v100.include_router(contact)
from .csrf import csrf
v100.include_router(csrf)
from .data import data
v100.include_router(data)
from .oauth import oauth
v100.include_router(oauth)