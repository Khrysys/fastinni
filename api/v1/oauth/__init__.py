from fastapi.routing import APIRouter

app = APIRouter(prefix="/oauth")

from .google import app as google
app.include_router(google)