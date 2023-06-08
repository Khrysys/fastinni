from fastapi.middleware.asyncexitstack import AsyncExitStackMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# from fastapi.middleware.trustedhost import TrustedHostMiddleware

from .extensions import *

# -----------------------
# | FASTAPI MIDDLEWARES |
# -----------------------
app.add_middleware(AsyncExitStackMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=CORS_ALLOWED_ORIGINS, 
                    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(GZipMiddleware, minimum_size=GZIP_MINIMUM_SIZE)
#app.add_middleware(TrustedHostMiddleware, allowed_hosts=TRUSTED_HOSTS) # uncomment these lines if you want that extra step in security
# app.add_middleware(HTTPSRedirectMiddleware)
