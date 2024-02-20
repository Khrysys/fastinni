from typing import Annotated
from fastapi import APIRouter, Depends, Form, Request, Response
from api.exceptions import LoginException

from ..security import check_csrf_token

from sqlmodel.ext.asyncio.session import AsyncSession
from ..db import User, db

app = APIRouter(prefix='/signup', tags=['Signup'])

@app.get("/")
# If additional form security is required it should be put here, additionally request and/or browser verification
# should be verified here
async def get_account_signup_info(): # type: ignore
    return 200


@app.post('/')
async def attempt_account_signup(
    display_name: Annotated[str, Form(alias='username')], 
    tag: Annotated[str, Form()], password: Annotated[str, Form()], 
    request: Request, 
    csrf: bool = Depends(check_csrf_token), 
    session: AsyncSession = Depends(db)
):
    user = None
    try:
        user = User.try_login_user(tag=tag, password=password, session=session)
    except LoginException: 
        pass

    if user is not None:
        # 409 here is Conflict, as described in this StackOverflow answer: https://stackoverflow.com/a/70371989
        return LoginException("User already exists", 409) 
    user = User(display_name=display_name, tag=tag)
    session.add(user)
    await session.commit()
    
@app.get('/tag')
async def check_if_tag_exists(tag: str, session: AsyncSession = Depends(db)):
    if await User.is_tag_available(tag, session):
        return Response(status_code=200)
    else:
        return Response(status_code=302)