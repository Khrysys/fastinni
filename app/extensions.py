from fastapi_csrf_protect import CsrfProtect
from fastapi_login import LoginManager
from fastapi_sql import SQLAlchemy
from pydantic import BaseModel

from . import config

settings = config.__dict__

class CsrfSettings(BaseModel):
    secret_key:str = settings['CSRF_SECRET_KEY']

@CsrfProtect.load_config # type: ignore
def get_csrf_config():
    return CsrfSettings()

login = LoginManager(settings['LOGIN_SECRET_KEY'], settings['LOGIN_PATH_URI'])
sqlalchemy = SQLAlchemy(database_uri=settings['SQLALCHEMY_DATABASE_URI'], session_options={})
