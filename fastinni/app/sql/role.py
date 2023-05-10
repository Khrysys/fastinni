from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

from . import RolesUsers


class Role(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    # Our Role has three fields, ID, name and description
    name: str
    description: str
    users: List['User'] = Relationship(back_populates='roles', link_model=RolesUsers) # type: ignore

    # __hash__ is required to avoid the exception TypeError: unhashable type: 'Role' when saving a User
    def __hash__(self):
        return hash(self.name)