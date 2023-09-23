from os import getenv

from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from sqlmodel import Session, select
from jwt import decode, encode
from .csrf import check_csrf_token
from ..db import engine
from ..db.user import User
from datetime import datetime

FASTINNI_LOGIN_SECRET = getenv("FASTINNI_LOGIN_SECRET", "secret")

account = APIRouter(prefix="/account")

@account.get('/user/{tag}', status_code=403)
async def account_index(request: Request, tag: str):
    if not check_csrf_token(request):
        return JSONResponse({'detail': 'Not Authorized'}, status_code=403)
    with Session(engine) as session:
        try:
            user = session.exec(select(User).where(User.tag==tag)).one()
        except:
            return JSONResponse({"detail": f"User @{tag} not found"}, status_code=404)
        
        
@account.post('/login')
async def login(request: Request):
    if not check_csrf_token(request):
        return JSONResponse({'detail': 'Not Authorized'}, status_code=403)
    
@account.post('/signup')
async def signup(request: Request):
    if not check_csrf_token(request):
        return JSONResponse({'detail': 'Not Authorized'}, status_code=403)
        
@account.get('/username-available/{username}')
async def get_username_availibility(request: Request, username: str):
    if not check_csrf_token(request):
        return JSONResponse({"detail": 'Not Authorized'}, status_code=403)
    
@account.get("/get-data")
async def get_current_user_data(request: Request):
    jwt = request.cookies.get('x-fastinni-login-jwt')
    if not check_csrf_token(request) or not jwt:
        return JSONResponse({'detail': 'Not Authorized'}, status_code=403)
    
    try:
        jwt = decode(jwt, FASTINNI_LOGIN_SECRET, algorithms=["HS256"]) # type: ignore

        with Session(engine) as session:
            user = session.exec(select(User).where(User.tag==jwt['tag']).where(User.name==jwt['username']).where(User.id==jwt['id'])).one()
            return {
                'username': user.name,
                'tag': user.tag,
                'email': user.email,
                'image': user.image
            }
    except:
        response = JSONResponse({'detail': 'invalid login-jwt'}, status_code=403)
        response.set_cookie('x-fastinni-login-jwt', '', expires=datetime.utcnow())
        return response
