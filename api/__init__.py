from os import getenv, urandom
from fastapi import FastAPI
from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

# The DB should be imported first
from . import db

load_dotenv()


# CSRF setup things
class CsrfSettings(BaseModel):
  secret_key:str = getenv('CSRF_SECRET', urandom(128).hex())
@CsrfProtect.load_config # type: ignore
def csrf_settings():
    return CsrfSettings()

api = FastAPI(
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

api.include_router(account)
api.include_router(security)
api.include_router(oauth)

# Import the exceptions here, since the app has been instantiated.
from . import exceptions

app = FastAPI(title="Fastinni", docs_url=None, redoc_url=None)
app.mount('/api', api)
app.mount('/', StaticFiles(directory='html', html=True))
