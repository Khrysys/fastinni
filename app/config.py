from os import getenv, urandom

from pydantic import BaseModel

LOGIN_SECRET_KEY = getenv('LOGIN_SECRET_KEY', urandom(128).hex())
LOGIN_PATH_URI = '/latest/user/login'
LOGIN_SALT_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
LOGIN_DEFAULT_PBKDF2_ITERATIONS = 600000

CORS_ALLOWED_ORIGINS = getenv('CORS_ALLOWED_ORIGINS', '127.0.0.1:5000;127.0.0.1:8000').split(';')
CSRF_SECRET_KEY = getenv('CSRF_SECRET_KEY', urandom(128).hex())
SQLALCHEMY_DATABASE_URI = 'postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
    getenv('SQLALCHEMY_USERNAME', 'postgres'), 
    getenv('SQLALCHEMY_PASSWORD', 'postgres'), 
    getenv('SQLALCHEMY_HOST', 'localhost'), 
    getenv('SQLALCHEMY_PORT', '5432'),
    getenv('SQLALCHEMY_DB_NAME', 'db-fastinni')
)

TRUSTED_HOSTS = getenv('TRUSTED_HOSTS', '127.0.0.1:5000;127.0.0.1:8000').split(';')
print(TRUSTED_HOSTS)
GZIP_MINIMUM_SIZE = int(getenv('GZIP_MINIMUM_SIZE', 1000))

GOOGLE_CLIENT_ID = getenv('GOOGLE_CLIENT_ID', '')
GOOGLE_CLIENT_SECRET = getenv('GOOGLE_CLIENT_SECRET', '')

class CsrfSettings(BaseModel):
    secret_key:str = CSRF_SECRET_KEY
    