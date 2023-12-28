from fastapi import APIRouter

latest = APIRouter(prefix="/latest", tags=["Latest"])

@latest.get("/status", tags=["Server Status"])
def get_latest_status():
    return 200

dev = APIRouter(prefix="/dev", tags=["In Development"])
from .v1 import oauth
dev.include_router(oauth)
latest.include_router(oauth)
from .v1 import account
dev.include_router(oauth)
latest.include_router(account)