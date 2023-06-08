from fastapi.routing import APIRouter

from ...routers import dev
from . import jwt

app = APIRouter(prefix='/auth')

app.include_router(jwt.app)

dev.include_router(app)