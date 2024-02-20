from typing import Annotated
from fastapi import APIRouter, Depends, Form, Request
from sqlmodel.ext.asyncio.session import AsyncSession

from ..db import User, db

from ..security import check_csrf_token

app = APIRouter(prefix='/login', tags=['Login'])

@app.get("/")
# If additional form security is required it should be put here, additionally request and browser verification
# should be verified here
async def get_account_login_info(): # type: ignore
    return 200

@app.post('/', )
async def attempt_account_login(
    tag: Annotated[str, Form()], 
    password: Annotated[str, Form()], 
    request: Request, 
    csrf:bool= Depends(check_csrf_token),
    session: AsyncSession = Depends(db)
): # type: ignore
    return User.generate_login_response(request, tag=tag, password=password, session=session)