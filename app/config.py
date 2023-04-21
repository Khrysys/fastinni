from os import getenv, urandom

from pydantic import BaseModel


class SqlAlchemySettings(BaseModel):
    SQLALCHEMY_SCHEMA = 'postgresql'
    SQLALCHEMY_DRIVER = 'asyncpg'
    SQLALCHEMY_USERNAME = getenv('SQLALCHEMY_USERNAME', 'postgres')
    SQLALCHEMY_PASSWORD = getenv('SQLALCHEMY_PASSWORD', 'postgres')
    SQLALCHEMY_HOST = getenv('SQLALCHEMY_HOST', 'localhost')
    SQLALCHEMY_PORT = getenv('SQLALCHEMY_PORT', '5432')
    SQLALCHEMY_DB_NAME = getenv('SQLALCHEMY_DB_NAME', 'db-fastinni')
        
    SQLALCHEMY_URL = '{}+{}://{}:{}@{}:{}/{}'.format(
        SQLALCHEMY_SCHEMA, SQLALCHEMY_DRIVER, SQLALCHEMY_USERNAME, 
        SQLALCHEMY_PASSWORD, SQLALCHEMY_HOST, SQLALCHEMY_PORT,
        SQLALCHEMY_DB_NAME
    )

class UserSecrets(BaseModel):
    reset_password_token_secret = getenv('RESET_PASSWORD_TOKEN_SECRET', urandom(128).hex())
    verification_token_secret = getenv('VERIFICATION_TOKEN_SECRET', urandom(128).hex())
    jwt_strategy_secret = getenv('JWT_STRATEGY_SECRET', urandom(128).hex())
    
class CsrfSettings(BaseModel):
    secret_key:str = getenv('CSRF_SECRET_KEY', urandom(128).hex())

class Settings(BaseModel):
    sqlalchemy_settings = SqlAlchemySettings()
    csrf_settings = CsrfSettings()
    user_secrets = UserSecrets()
    