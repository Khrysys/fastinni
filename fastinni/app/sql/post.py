from datetime import datetime
from typing import List, Optional

import humanize
from sqlmodel import Field, Relationship, SQLModel

from . import TagsPosts


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    writer_id: Optional[int] = Field(default=None, foreign_key='user.id')
    writer: Optional['User'] = Relationship(back_populates='posts') # type: ignore
    title: str
    subtitle: str
    body: str 
    image: str
    slug: str
    publish_date: datetime = Field(default=datetime.utcnow())
    live: bool
    tags: List["Tag"] = Relationship(back_populates='posts', link_model=TagsPosts) # type: ignore
      
    @property
    def pubdate(self):
        """Return the date in readable English """
        return humanize.naturaltime(self.publish_date) 

    def __repr__(self):
        if self.title:
            return f'<Post {self.title}>'
        else: return super().__repr__()