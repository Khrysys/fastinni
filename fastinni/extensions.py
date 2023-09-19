from fastapi_csrf_protect import CsrfProtect
from os import getenv, urandom
from fastapi.middleware.asyncexitstack import AsyncExitStackMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_mail import FastMail, ConnectionConfig
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .settings import *

@CsrfProtect.load_config # type: ignore
def get_csrf_config():
    return [
        ("secret_key", FASTINNI_CSRF_TOKEN),
        ("cookie_samesite", FASTINNI_CSRF_COOKIE_SAMESITE),
        ("cookie_secure", FASTINNI_CSRF_COOKIE_SECURE),
        ("cookie_httponly", FASTINNI_CSRF_COOKIE_HTTPONLY)
    ]

csrf = CsrfProtect()

mail = FastMail(ConnectionConfig(
        MAIL_USERNAME=FASTINNI_MAIL_USERNAME,
        MAIL_PASSWORD=FASTINNI_MAIL_PASSWORD,
        MAIL_PORT=FASTINNI_MAIL_PORT, # type: ignore
        MAIL_SERVER=FASTINNI_MAIL_SERVER,
        MAIL_STARTTLS=FASTINNI_MAIL_STARTTLS, # type: ignore
        MAIL_SSL_TLS=FASTINNI_MAIL_SSL_TLS, # type: ignore
        MAIL_DEBUG=FASTINNI_MAIL_DEBUG,
        MAIL_FROM=FASTINNI_MAIL_FROM # type: ignore
    )
)