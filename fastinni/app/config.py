# this file just loads things from config.json. Nothing more, nothing less

from os import getenv, urandom
from functools import lru_cache
from requests import get
from json import load

from pydantic import BaseModel

config_file = open('config.json')
config = load(config_file)

@lru_cache
def get_google_provider_cfg() -> dict:
    return get("https://accounts.google.com/.well-known/openid-configuration").json()

LOGIN_SECRET_KEY = getenv('LOGIN_SECRET_KEY', urandom(128).hex()) # type: ignore
LOGIN_PATH_URI = '/latest/user/login'
LOGIN_SALT_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
LOGIN_DEFAULT_PBKDF2_ITERATIONS = 600000

CSRF_SECRET_KEY = getenv('CSRF_SECRET_KEY', urandom(128).hex())
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
    getenv('SQLALCHEMY_USERNAME', 'postgres'), 
    getenv('SQLALCHEMY_PASSWORD', 'postgres'), 
    getenv('SQLALCHEMY_HOST', 'localhost'), 
    getenv('SQLALCHEMY_PORT', '5432'),
    getenv('SQLALCHEMY_DB_NAME', 'db-fastinni')
)

CORS_ALLOWED_ORIGINS = config['fastapi']['middlewares']['cors']['allowed_origins']
TRUSTED_HOSTS = getenv('TRUSTED_HOSTS', '127.0.0.1:5000;127.0.0.1:8000').split(';')
GZIP_MINIMUM_SIZE = int(getenv('GZIP_MINIMUM_SIZE', 1000)) # type: ignore

GOOGLE_CLIENT_ID = getenv('GOOGLE_CLIENT_ID', '')
GOOGLE_CLIENT_SECRET = getenv('GOOGLE_CLIENT_SECRET', '')

SESSION_SECRET_KEY = getenv('SESSION_SECRET_KEY', urandom(128).hex())

class CsrfSettings(BaseModel):
    secret_key:str = config['fastapi-csrf']['secret_key']
    