from fastapi import FastAPI


app = FastAPI(
    debug=False,
    title="Fastinni API",
    summary="",
    description="",
    version="1.0.0",
    docs_url=None, 
    redoc_url='/docs'
)

from .account import app as account
app.include_router(account)
from .security import app as security
app.include_router(security)
