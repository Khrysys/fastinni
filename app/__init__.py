from functools import lru_cache

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

from .api.v1 import v1 as v1_router
from .config import Settings

@lru_cache
def get_settings():
    return settings

settings = Settings()
fastapi = FastAPI()
fastapi.include_router(v1_router)
engine = create_engine(get_settings().sqlalchemy_settings.SQLALCHEMY_URL)
engine.connect()
db = sessionmaker(engine)
db_metadata = MetaData()

@CsrfProtect.load_config
def get_csrf_load_config():
    return get_settings().csrf_settings

@lru_cache
def get_settings():
    return settings

@fastapi.get('/')
async def get_():
    return {'status': 'ok'}

@fastapi.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
  return JSONResponse(status_code=exc.status_code, content={ 'detail':  exc.message })

from . import tables