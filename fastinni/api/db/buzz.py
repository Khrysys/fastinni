from typing import Optional

from sqlmodel import SQLModel, Relationship, Field

class Buzz(SQLModel, table=True):
    id: Optional[int] = Field(default=None)

    user_id: Optional[int] = Field(foreign_key="user.id", nullable=True)
    post_id: Optional[int] = Field(foreign_key="post.id", nullable=True)

    title: str
    body: str