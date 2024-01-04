from typing import List, Optional
from sqlmodel import Field, SQLModel

from .access_client import AccessClient, PossibleScopes
from .user import User

class AuthorizationToken(SQLModel, table=True):
    client_id: Optional[int] = Field(primary_key=True, foreign_key=AccessClient.id)
    user_id: Optional[int] = Field(primary_key=True, foreign_key=User.id)
    scopes: List[PossibleScopes]
    challenge: str = Field(min_length=128, unique=True)
    challenge_method: str = Field(max_length=6)