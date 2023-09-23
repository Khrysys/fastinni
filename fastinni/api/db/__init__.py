from sqlmodel import create_engine
from ...settings import FASTINNI_DB_URL

engine = create_engine(FASTINNI_DB_URL)

from . import *