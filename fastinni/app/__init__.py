from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI, Request
from fastapi.middleware.asyncexitstack import AsyncExitStackMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from fastapi_jwt_login import JWTLogin
from oauthlib.oauth2 import WebApplicationClient
from sqlmodel import create_engine
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware

from .config import *


@CsrfProtect.load_config # type: ignore
def get_csrf_config():
    return CsrfSettings()

app = FastAPI(title='Fastinni', version = "Highest Version: 1.0.0", docs_url=None, redoc_url='/docs')
db = create_engine(SQLALCHEMY_DATABASE_URI)
jwt = JWTLogin(LOGIN_SECRET_KEY)

config_data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID, 'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET}
starlette_config = Config(environ=config_data)
oauth = OAuth(starlette_config)
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)

# -----------------------
# | FASTAPI MIDDLEWARES |
# -----------------------
app.add_middleware(AsyncExitStackMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=CORS_ALLOWED_ORIGINS, 
                    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(GZipMiddleware, minimum_size=GZIP_MINIMUM_SIZE)
#app.add_middleware(TrustedHostMiddleware, allowed_hosts=TRUSTED_HOSTS) # uncomment these lines if you want that extra step in security
# app.add_middleware(HTTPSRedirectMiddleware)

# -------------------------
# | STARLETTE MIDDLEWARES |
# -------------------------
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET_KEY)

# ----------------------
# | EXCEPTION HANDLERS |
# ----------------------
@app.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
    return JSONResponse(status_code=exc.status_code, content={ 'detail':  exc.message })
    
from . import v100
# ---------------
# | API ROUTERS |
# ---------------
from .routers import dev, latest

app.include_router(dev)
app.include_router(latest)
app.include_router(v100.app)