from fastapi import APIRouter

v1 = APIRouter(prefix='/v1')

from . import csrf, user