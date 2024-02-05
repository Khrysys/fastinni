from os import getenv
from typing import Annotated, Any, Optional
from fastapi import APIRouter, Cookie, Request
from jwt import decode

from ..db import User

app = APIRouter(prefix='/account', tags=['Account'])

from .login import app as login
app.include_router(login)

async def try_login_token(login_token: Annotated[Optional[str], Cookie()] = None) -> Optional[User]:
    try:
        data: dict[str, Any] = decode(login_token, getenv('LOGIN_SECRET'), algorithms=['HS256'], verify=True) # type: ignore
        return User.try_login_user(tag=data.get('tag'), email=data.get('email'), password=data.get('password'), google_id=data.get('google_id'))
    except:
        return None