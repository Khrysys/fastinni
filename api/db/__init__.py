from os import getenv
from sqlmodel import SQLModel, create_engine

db_url = getenv("DB_URL", 'postgresql+psycopg://postgres:postgres@127.0.0.1:5432/db-fastinni')

engine = create_engine(getenv("DB_URL", 'postgresql+psycopg://postgres:postgres@127.0.0.1:5432/db-fastinni'))

from .user import User

SQLModel.metadata.create_all(engine)