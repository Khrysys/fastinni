from fastapi import FastAPI, Request
from fastapi.middleware.asyncexitstack import AsyncExitStackMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi_csrf_protect.exceptions import CsrfProtectError

from .extensions import sqlalchemy

app = FastAPI(version = "0.1.0", redoc_url=None, docs_url=None, openapi_url=None)

# -----------------------
# | FASTAPI MIDDLEWARES |
# -----------------------
app.add_middleware(AsyncExitStackMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=extensions.settings['CORS_ALLOWED_ORIGINS'], 
                    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(GZipMiddleware, minimum_size=extensions.settings['GZIP_MINIMUM_SIZE'])
app.add_middleware(TrustedHostMiddleware, allowed_hosts=extensions.settings['TRUSTED_HOSTS'])

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
    
@app.get("/docs", include_in_schema=False)
async def get_documentation(request: Request):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="KhrySystem API Documentation")

@app.get("/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(title=app.title, version=app.version, routes=app.routes)
