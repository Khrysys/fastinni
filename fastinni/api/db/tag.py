from typing import Optional, List


from sqlmodel import SQLModel, Relationship, Field

from .tags_posts import TagsPosts

class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    posts: List["Post"] = Relationship(back_populates="tags", link_model=TagsPosts) # type: ignore
