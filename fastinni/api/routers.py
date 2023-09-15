from fastapi.routing import APIRouter

latest = APIRouter(prefix="/latest")
@latest.get("/")
async def latest_index():
    return {}
dev = APIRouter(prefix="/dev")
