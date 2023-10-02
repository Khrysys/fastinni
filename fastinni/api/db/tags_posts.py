from typing import Optional

from sqlmodel import SQLModel, Field

class TagsPosts(SQLModel, table=True):
    post_id: int = Field(foreign_key='post.id', primary_key=True, nullable=False)
    tag_id: int = Field(foreign_key='tag.id', primary_key=True, nullable=False)