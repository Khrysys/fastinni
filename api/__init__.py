from os import urandom
from fastapi import FastAPI
from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel

print('here', flush=True)
# The DB should be imported first
from .db import *



# CSRF setup things
class CsrfSettings(BaseModel):
  secret_key:str = getenv('CSRF_SECRET', urandom(128).hex())
@CsrfProtect.load_config # type: ignore
def csrf_settings():
    return CsrfSettings()

app = FastAPI(
    debug=False,
    title="Fastinni API",
    summary="A FastAPI / React SPWA Example",
    description="",
    version="1.0.0",
    docs_url=None, 
    redoc_url='/docs'
)

from . import exceptions
from .account import app as account
from .oauth import app as oauth
from .security import app as security

app.include_router(account)
app.include_router(security)
app.include_router(oauth)

# Import the exceptions here, since the app has been instantiated.
from . import exceptions
