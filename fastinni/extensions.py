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