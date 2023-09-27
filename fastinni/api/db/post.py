from typing import Optional, List
from datetime import datetime
from humanize import naturaltime

from sqlmodel import SQLModel, Relationship, Field

from .tags_posts import TagsPosts
from .tag import Tag

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key='user.id')
    title: Optional[str]
    subtitle: Optional[str]
    body: Optional[str]
    image: Optional[str]
    
    publish_date: Optional[datetime] = Field(default=datetime.utcnow)

    tags: List[Tag] = Relationship(back_populates="posts", link_model=TagsPosts)

    @property
    def pubdate(self):
        return naturaltime(self.publish_date) # type: ignore