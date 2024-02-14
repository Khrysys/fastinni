from typing import Annotated
from fastapi import APIRouter, Body, Cookie, Depends, Form, Request
from fastapi_csrf_protect import CsrfProtect

from ..db import User

app = APIRouter(prefix='/login', tags=['Login'])

@app.get("/")
# If additional form security is required it should be put here, additionally request and browser verification
# should be verified here
async def get_account_login_info(): # type: ignore
    return 200

@app.post('/')
async def attempt_account_login(tag: Annotated[str, Form()], password: Annotated[str, Form()], request: Request, csrf_protect:CsrfProtect = Depends()):
    await csrf_protect.validate_csrf(request)

    return User.generate_login_response(request, tag=tag, password=password)