from fastapi import FastAPI
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

from . import db # type: ignore
from . import exceptions # type: ignore
from .account import app as account # type: ignore
from .oauth import app as oauth # type: ignore
from .security import app as security # type: ignore


app = FastAPI(title="Fastinni", docs_url=None, redoc_url=None)
app.mount('/api', api)
app.mount('/', StaticFiles(directory='html', html=True))

