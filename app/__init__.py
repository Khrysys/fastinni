from fastapi import FastAPI, Request
from fastapi.middleware.asyncexitstack import AsyncExitStackMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from fastapi_login import LoginManager
from fastapi_sql import SQLAlchemy

from .config import *

@CsrfProtect.load_config # type: ignore
def get_csrf_config():
    return CsrfSettings()



app = FastAPI(title='KSSI', version = "Highest Version: 1.0.0", docs_url=None, redoc_url='/docs')
login = LoginManager(LOGIN_SECRET_KEY, LOGIN_PATH_URI)
sqlalchemy = SQLAlchemy(app=app, database_uri=SQLALCHEMY_DATABASE_URI)

# -----------------------
# | FASTAPI MIDDLEWARES |
# -----------------------
app.add_middleware(AsyncExitStackMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=CORS_ALLOWED_ORIGINS, 
                    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(GZipMiddleware, minimum_size=GZIP_MINIMUM_SIZE)
#app.add_middleware(TrustedHostMiddleware, allowed_hosts=TRUSTED_HOSTS) # uncomment these lines if you want that extra step in security
# app.add_middleware(HTTPSRedirectMiddleware)

# ----------------------
# | CUSTOM MIDDLEWARES |
# ----------------------
app.add_middleware(sqlalchemy.middleware, sqlalchemy=sqlalchemy)

# ----------------------
# | EXCEPTION HANDLERS |
# ----------------------
@app.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
    return JSONResponse(status_code=exc.status_code, content={ 'detail':  exc.message })
    
# ---------------
# | API ROUTERS |
# ---------------
from .routers import dev, latest
from .v100 import v100
app.include_router(dev)
app.include_router(latest)
app.include_router(v100)