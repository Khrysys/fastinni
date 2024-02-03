from fastapi import APIRouter


app = APIRouter(prefix="/oauth", tags=['OAuth2 / OpenID Endpoints'])

from .google import app as google

app.include_router(google)