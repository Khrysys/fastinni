


from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, BigInteger
class Base(DeclarativeBase):
    id = Column('id', BigInteger, primary_key=True)


