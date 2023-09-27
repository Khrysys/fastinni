from typing import Optional

from sqlmodel import SQLModel, Field

class FriendsList(SQLModel, table=True):
    a_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True, nullable=False)
    b_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True, nullable=False)