from .user import User
from sqlmodel import SQLModel, create_engine
from os import getenv

engine = create_engine(getenv("DB_URL"), echo=True) # type: ignore

SQLModel.metadata.create_all(engine)