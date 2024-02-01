from fastapi import APIRouter


app = APIRouter(prefix='/account', tags=['Account'])

from .login import app as login
app.include_router(login)