from typing import Optional

from sqlmodel import SQLModel, Field

class FriendsList(SQLModel, table=True):
    a_id: int = Field(foreign_key="user.id", primary_key=True, nullable=False) # type: ignore
    b_id: int = Field(foreign_key="user.id", primary_key=True, nullable=False) # type: ignore