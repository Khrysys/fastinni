from os import getenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.asyncexitstack import AsyncExitStackMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

async def index():
    return {}

from .extensions import *

def create_app():
    api = FastAPI(debug=True, title="Fastinni API")
    app = FastAPI(debug=True, tile="Fastinni")

    # -----------------------
    # | FASTAPI MIDDLEWARES |
    # -----------------------

    from .api.db import engine
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)


    api.add_middleware(AsyncExitStackMiddleware)
    api.add_middleware(CORSMiddleware, allow_origins=getenv("FASTAPI_CORS_ALLOWED_ORIGINS", "127.0.0.1:5000").split(";"), 
                        allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    api.add_middleware(GZipMiddleware, minimum_size=int(getenv("FASTAPI_GZIP+MINIMUM_SIZE", "1000")))
    #app.add_middleware(TrustedHostMiddleware, allowed_hosts=TRUSTED_HOSTS) # uncomment these lines if you want that extra step in security
    app.add_middleware(HTTPSRedirectMiddleware)

    # ----------------
    # - APP ASSEMBLY |
    # ----------------
    app.mount(path="/api", app=api, name='API')
    app.mount(path='/', app=StaticFiles(directory='fastinni/pages', html=True), name='Pages') # type: ignore
    
    from .api.routers import latest, dev
    api.include_router(latest, tags=['Latest'])
    api.include_router(dev, tags=['In Development'])
    from .api.v100 import v100
    api.include_router(v100, prefix='/v100', tags=['Version 1.0.0'])
    return app
