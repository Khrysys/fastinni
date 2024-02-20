from os import getenv
from typing import Annotated, Any, Optional
from fastapi import APIRouter, Cookie, Depends
from jwt import decode

from sqlmodel.ext.asyncio.session import AsyncSession
from ..db import User, db

app = APIRouter(prefix='/account', tags=['Account'])

from .login import app as login
app.include_router(login)
from .signup import app as signup
app.include_router(signup)

async def try_login_token(login_token: Annotated[str, Cookie()], session: AsyncSession = Depends(db)) -> Optional[User]:
    try:
        data: dict[str, Any] = decode(login_token, getenv('LOGIN_SECRET'), algorithms=['HS256'], verify=True) # type: ignore
        return await User.try_login_user(tag=data.get('tag'), email=data.get('email'), password=data.get('password'), google_id=data.get('google_id'), session=session)
    except:
        return None