from fastapi import APIRouter

v1 = APIRouter(prefix='/v1', tags=['Version 1.0.0'])

from . import csrf, user