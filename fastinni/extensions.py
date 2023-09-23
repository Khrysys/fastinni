
from fastapi_mail import FastMail, ConnectionConfig
from .settings import *

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