import uuid
from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

from . import RolesUsers, Post, Role


def uuid_generator():
    return uuid.uuid4().hex

class User(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("username"),
        UniqueConstraint("email"),
        UniqueConstraint("phone"),
        UniqueConstraint("google_token")
    )
    
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: Optional[str]
    password_hash: Optional[str]
    phone: Optional[str]
    """While there are many ways to store phone numbers, here a string is being used."""
    
    # PERSONALIZATION
    address: Optional[str]
    about: Optional[str]
    image: Optional[str]
    """Name of file that's kept in the user's folder"""
    
    # CONNECTIONS
    google_token: Optional[str]
    
    # TOGGLES
    active: bool = Field(default=False)
    public_profile: bool = Field(default=False)
    google_signin: bool = Field(default=False)
    # DATES
    confirmed_at: Optional[datetime]
    last_seen: Optional[datetime]
    creation: datetime = Field(default=datetime.utcnow())
    """This property is automatically updated in the `before_request` function as defined in the app's `__init__.py` file."""
    posts: List['Post'] = Relationship(back_populates='writer') 
    roles: List['Role'] = Relationship(back_populates='users', link_model=RolesUsers)
    
    def __str__(self):
        return 'User <{}, {}>'.format(self.id, self.username)
   