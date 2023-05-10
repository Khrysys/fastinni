from fastapi.routing import APIRouter

dev = APIRouter(prefix='/dev', tags=['In Development'])
latest = APIRouter(prefix='/latest', tags=['Latest'])