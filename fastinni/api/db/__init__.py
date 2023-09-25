from sqlmodel import create_engine
from ...settings import FASTINNI_DB_URL

engine = create_engine(FASTINNI_DB_URL)

from .buzz import Buzz
from .friends_list import FriendsList
from .post import Post
from .role import Role
from .roles_users import RolesUsers
from .tag import Tag
from .tags_posts import TagsPosts
from .user import User