from os import getenv
from sqlmodel import SQLModel, create_engine

engine = create_engine(getenv("DB_URL")) # type: ignore

from .user import User

SQLModel.metadata.create_all(engine)