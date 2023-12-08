from fastapi import APIRouter

app = APIRouter(prefix="/v1", tags=['Version 1'])

from .oauth import app as oauth
app.include_router(oauth)