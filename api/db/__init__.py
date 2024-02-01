from os import getenv
from sqlmodel import SQLModel, create_engine


engine = create_engine(getenv("DB_URL")) # type: ignore
SQLModel.metadata.create_all(engine)