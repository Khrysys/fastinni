from fastapi import APIRouter

v100 = APIRouter(prefix='/v1', tags=['Version 1.0.0'])

from . import csrf, user