from fastapi.routing import APIRouter

google = APIRouter(prefix="/google")

@google.get('/')
async def index():
    return {}