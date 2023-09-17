from datetime import datetime

from fastapi.routing import APIRouter

build_time = str(datetime.now())
latest = APIRouter(prefix="/latest")
@latest.get("/")
def index():
    return {"Server Build": build_time}
dev = APIRouter(prefix="/dev")
