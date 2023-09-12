from fastapi_csrf_protect import CsrfProtect
from os import getenv, urandom
from fastapi.middleware.asyncexitstack import AsyncExitStackMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# from fastapi.middleware.trustedhost import TrustedHostMiddleware

@CsrfProtect.load_config # type: ignore
def get_csrf_config():
    return [
        ("secret_key", getenv('FASTAPI_CSRF_TOKEN', str(urandom(128).hex()))),
        ("cookie_samesite", 'none'),
        ("cookie_secure", True)
    ]

csrf = CsrfProtect()

from . import app

# -----------------------
# | FASTAPI MIDDLEWARES |
# -----------------------
app.add_middleware(AsyncExitStackMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=getenv("FASTAPI_CORS_ALLOWED_ORIGINS", "127.0.0.1:5000").split(";"), 
                    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(GZipMiddleware, minimum_size=int(getenv("FASTAPI_GZIP+MINIMUM_SIZE", "1000")))
#app.add_middleware(TrustedHostMiddleware, allowed_hosts=TRUSTED_HOSTS) # uncomment these lines if you want that extra step in security
# app.add_middleware(HTTPSRedirectMiddleware)