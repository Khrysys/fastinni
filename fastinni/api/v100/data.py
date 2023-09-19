from fastapi.routing import APIRouter

data = APIRouter()

@data.get('/')
def index():
    return {"detail": "found"}