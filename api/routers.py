from fastapi import APIRouter

latest = APIRouter(prefix="/latest", tags=["Latest"])

@latest.get("/status", tags=["Server Status"])
def get_latest_status():
    return 200

from .v1 import oauth
latest.include_router(oauth)
from .v1 import account
latest.include_router(account)