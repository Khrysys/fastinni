from typing import Optional

from sqlmodel import Field, SQLModel


class RolesUsers(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key='user.id', primary_key=True)
    role_id: Optional[int] = Field(default=None, foreign_key='role.id', primary_key=True)

class TagsPosts(SQLModel, table=True):
    post_id: Optional[int] = Field(default=None, foreign_key='post.id', primary_key=True)
    tag_id: Optional[int] = Field(default=None, foreign_key='tag.id', primary_key=True)