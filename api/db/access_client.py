from enum import StrEnum
from typing import List, Optional
from sqlmodel import Column, Enum, Field, Relationship, SQLModel

class GrantTypes(StrEnum):
    authorization_code = 'authorization_code'

class ResponseTypes(StrEnum):
    code = 'code'
    authorization_code = 'authorization_code'

class PossibleScopes(StrEnum):
    pass

class AccessClient(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, unique=True, nullable=False)
    user: Optional["User"] = Relationship(back_populates='access_clients') # type: ignore
    user_id: Optional[int] = Field(primary_key=True, foreign_key="user.id")
    grant_type: GrantTypes
    response_type: ResponseTypes
    scopes: List["PossibleScopes"]
    default_scopes: List["PossibleScopes"]
    redirect_uris: List[str]
    default_redirect_uri: str
