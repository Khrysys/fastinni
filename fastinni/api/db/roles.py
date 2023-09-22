from typing import Optional, List
from sqlmodel import SQLModel, Relationship, Field
from .roles_users import RolesUsers
class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    description: Optional[str]
    users: List["User"] = Relationship(back_populates="roles", link_model=RolesUsers) # type: ignore