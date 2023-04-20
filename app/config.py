from pydantic import BaseModel
from os import getenv, urandom

class SqlAlchemySettings(BaseModel):
    SQLALCHEMY_SCHEMA = getenv('SQLALCHEMY_SCHEMA', 'postgresql')
    SQLALCHEMY_DRIVER = getenv('SQLALCHEMY_DRIVER', 'psycopg2')
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
    
class CsrfSettings(BaseModel):
    secret_key:str = getenv('CSRF_SECRET_KEY', urandom(128).hex())

class Settings(BaseModel):
    sqlalchemy_settings = SqlAlchemySettings()
    csrf_settings = CsrfSettings()
    