from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import query

from .routers import dev 
from ..db import sessionmaker
from ..db.user import User
from ..security import check_password_hash
from sqlalchemy import Result
from os import getenv
from jwt import encode

FASTINNI_LOGIN_SECRET = getenv("FASTINNI_LOGIN_SECRET")

account = APIRouter(prefix="/account")

@account.get('/{tag}')
async def account_index(request: Request, tag: str):
    async with sessionmaker.begin() as session:
        try:
            user = await session.execute(select(User).where(User.tag == tag))
        except:
            return JSONResponse({tag: "not found"}, status_code=404)
    return User.get_profile(user)
        
@account.post('/login')
async def login(request: Request):
    data = await request.json()
    
    async with sessionmaker.begin() as session:
        try: 
            user = await session.execute(select(User).where(User.tag == data['tag']))
            user = user.one_or_none() # type: ignore
        except: 
            return JSONResponse({data['tag']: "not found"}, status_code=404)
        if(check_password_hash(user.password_hash, data['password'])): # type: ignore
            return JSONResponse({"x-fastinni-login-jwt": 'success', 'value': encode({'tag': user.tag, 'username': user.username, 'id': user.id}, FASTINNI_LOGIN_SECRET, algorithm="HS256")}, status_code=200) # type: ignore
        return JSONResponse({data['tag']: "invalid"}, status_code=403)
    
@account.post('/signup')
async def signup(request: Request):
    data = await(request.json())
    async with sessionmaker.begin() as session:
        try: 
            user = User(username=data['username'], tag=data['tag'], phone=data.get('phone'))
            session.add(user)
            await session.commit()
            return JSONResponse({"x-fastinni-login-jwt": encode({'tag': user.tag, 'username': user.username, 'id': user.id}, FASTINNI_LOGIN_SECRET, algorithm="HS256")}, status_code=200) # type: ignore
        except:
            return JSONResponse({'detail': 'data_invalid'}, status_code=400)
        