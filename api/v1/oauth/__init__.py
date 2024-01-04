from fastapi.routing import APIRouter
import oauthlib

oauthlib.O

app = APIRouter(prefix="/oauth")

from .google import app as google
app.include_router(google)