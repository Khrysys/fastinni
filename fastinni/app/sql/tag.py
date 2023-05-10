from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

from . import TagsPosts


class Tag(SQLModel, table=True): # type: ignore
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    posts: List['Post'] = Relationship(back_populates='tags', link_model=TagsPosts) # type: ignore

    def __repr__(self):
        return self.name