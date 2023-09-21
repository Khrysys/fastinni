from sqlmodel import create_engine, SQLModel
from ...settings import FASTINNI_DB_URL

engine = create_engine(FASTINNI_DB_URL)

