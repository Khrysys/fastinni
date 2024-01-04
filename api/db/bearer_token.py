from datetime import datetime
import secrets
import string
from typing import List, Optional
from sqlmodel import Field, SQLModel

from .access_client import AccessClient, PossibleScopes
from .user import User

def gen_token():
    return ''.join(secrets.choice(string.ascii_letters + string.digits)
              for i in range(128))

class BearerToken(SQLModel, table=True):
    client_id: Optional[int] = Field(primary_key=True, foreign_key=AccessClient.id)
    user_id: Optional[int] = Field(primary_key=True, foreign_key=User.id)
    scopes: List[PossibleScopes]
    access_token: Optional[str] = Field(default_factory=gen_token, unique=True)
    refresh_token: Optional[str] = Field(default_factory=gen_token, unique=True)
    expires_at: datetime