from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, Session, SQLModel, select, UniqueConstraint
from .roles_users import RolesUsers
from .role import Role
from .friends_list import FriendsList

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)

    name: Optional[str]
    tag: str = Field(unique=True)

    phone: Optional[str] = Field(unique=True)
    public_phone: Optional[bool] = Field(default=True)
    email: Optional[str] = Field(unique=True)
    public_email: Optional[bool] = Field(default=True)
    address: Optional[str]
    public_address: Optional[bool] = Field(default=True)
    about: Optional[str]
    image: Optional[str]
    password_hash: Optional[str]

    active: Optional[bool] = Field(default=True)
    public_profile: Optional[bool] = Field(default=True)

    confirmed_at: Optional[datetime]
    last_seen: Optional[datetime]

    roles: List[Role] = Relationship(back_populates="users", link_model=RolesUsers)
    friends: List["User"] = Relationship(back_populates="friends", link_model=FriendsList)

    def get_profile(self):
        if not self.public_profile:
            return
        return {
            'id': self.id,
            'name': self.name, 
            'tag': self.tag,
            'phone': self.phone if self.public_phone else None,
            'email': self.email if self.public_email else None,
            'address': self.address if self.public_address else None,
            'about': self.about,
            'image': self.image,
            'active': self.active,
            'confirmed_at': self.confirmed_at,
            'last_seen': self.last_seen
        }


from . import engine

def add_user_if_not_found(tag: str) -> User:
    try:
        with Session(engine) as session:
            user = session.execute(select(User).where(User.tag==tag)).one()
    except:
        user = User(tag=tag) # type: ignore
        with Session(engine) as session:
            session.add(user)
            session.commit()
    return user
            