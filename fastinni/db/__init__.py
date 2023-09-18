from os import getenv

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer


class Base(AsyncAttrs, DeclarativeBase):
    id = Column("id", Integer, primary_key=True, nullable=False, unique=True)

db = create_async_engine(getenv("FASTAPI_DB_URL")) # type: ignore
sessionmaker = async_sessionmaker(db)

