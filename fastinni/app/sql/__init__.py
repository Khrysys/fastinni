from sqlmodel import SQLModel
from .links import RolesUsers, TagsPosts
from .post import Post
from .role import Role
from .tag import Tag
from .user import User
from .. import db
SQLModel.metadata.create_all(db)
