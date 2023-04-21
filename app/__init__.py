from functools import lru_cache

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from fastapi.openapi.docs import get_swagger_ui_html

from .config import Settings
from .v1 import v1 as v1_router


@lru_cache
def get_settings():
    return settings

settings = Settings()
#print('Current Settings: \n{}'.format(settings.dict()))
fastapi = FastAPI()
fastapi.include_router(v1_router)

engine = create_async_engine(get_settings().sqlalchemy_settings.SQLALCHEMY_URL)
engine.connect()
async_session_maker = async_sessionmaker(engine)



@CsrfProtect.load_config
def get_csrf_load_config():
    return get_settings().csrf_settings

@fastapi.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(req: Request):
    root_path = req.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + fastapi.openapi_url
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title="API",
    )

'''
@fastapi.get('/')
async def get_():
    return {'status': 'ok'}

@fastapi.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
  return JSONResponse(status_code=exc.status_code, content={ 'detail':  exc.message })

from . import tables
from .tables.user import fastapi_users, auth_backend, UserRead, UserCreate, UserUpdate

fastapi.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
fastapi.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
fastapi.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
fastapi.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
fastapi.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)'''