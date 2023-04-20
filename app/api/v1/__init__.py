from fastapi import APIRouter

v1 = APIRouter(prefix='/api/v1')

from . import csrf, user