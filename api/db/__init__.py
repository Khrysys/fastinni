from sqlmodel import SQLModel, create_engine
from os import getenv

engine = create_engine(getenv("DB_URL")) # type: ignore

from .user import User
from .access_client import AccessClient
from .authorization_token import AuthorizationToken
from .bearer_token import BearerToken


SQLModel.metadata.create_all(engine)