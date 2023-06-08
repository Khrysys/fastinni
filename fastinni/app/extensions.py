from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
from fastapi_csrf_protect import CsrfProtect
from fastapi_jwt_login import JWTLogin
from sqlalchemy.ext.asyncio import create_async_engine
from starlette.config import Config
from slowapi import Limiter
from slowapi.util import get_remote_address

from .config import *


@CsrfProtect.load_config # type: ignore
def get_csrf_config():
    return CsrfSettings()

app = FastAPI(title='Fastinni', version = "Highest Version: 1.0.0", docs_url=None, redoc_url='/docs')
db = create_async_engine(SQLALCHEMY_DATABASE_URI, echo=True, future=True)
jwt = JWTLogin(LOGIN_SECRET_KEY)
limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter

config_data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID, 'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET}
starlette_config = Config(environ=config_data)
oauth = OAuth(starlette_config)
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)
