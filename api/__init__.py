from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
load_dotenv()

api = FastAPI(
    debug=False,
    title="Fastinni API",
    summary="A FastAPI / React SPWA Example",
    description="",
    version="1.0.0",
    docs_url=None, 
    redoc_url='/docs'
)

from . import db
from . import exceptions
from .account import app as account
from .oauth import app as oauth
from .security import app as security

api.include_router(account)
api.include_router(security)
api.include_router(oauth)

app = FastAPI(title="Fastinni", docs_url=None, redoc_url=None)
app.mount('/api', api)
app.mount('/', StaticFiles(directory='html', html=True))

