from os import getenv

from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from ...security import check_password_hash
from ..db.user import User

FASTINNI_LOGIN_SECRET = getenv("FASTINNI_LOGIN_SECRET")

account = APIRouter(prefix="/account")

@account.get('/{tag}')
async def account_index(request: Request, tag: str):
    return {}
        
@account.post('/login')
async def login(request: Request):
    return {}
    
@account.post('/signup')
async def signup(request: Request):
    return {}
        
@account.get('/username-available/{username}')
async def get_username_availibility(request: Request, username: str):
    return {}