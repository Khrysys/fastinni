from fastapi import APIRouter

latest = APIRouter(prefix="/latest", tags=["Latest"])
dev = APIRouter(prefix="/dev", tags=["In Development"])
from .v1 import oauth
dev.include_router(oauth)