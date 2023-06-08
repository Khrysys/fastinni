import uuid
from datetime import datetime
from typing import List, Optional, Any
from fastapi.responses import JSONResponse

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
    google_uid: Optional[str]
    google_token: Optional[str]
    google_signin: bool = Field(default=False)
    
    # TOGGLES
    active: bool = Field(default=False)
    public_profile: bool = Field(default=True)
    public_email: bool = Field(default=False)
    public_phone: bool = Field(default=False)
    public_address: bool = Field(default=False)
    
    # DATES
    confirmed_at: Optional[datetime]
    last_seen: Optional[datetime]
    creation: datetime = Field(default=datetime.utcnow())
    
    # Relationships
    posts: List['Post'] = Relationship(back_populates='writer') 
    roles: List['Role'] = Relationship(back_populates='users', link_model=RolesUsers)
    
    def __str__(self):
        return 'User <{}, {}>'.format(self.id, self.username)
    
    def validate_google_data(self, data: dict[str, Any]) -> bool:
        return (data['mode'] == 'google' and 
                data['id'] == self.id and 
                data['google_token'] == self.google_token and 
                data['google_uid'] == self.google_uid)
        
    def generate_google_data(self) -> dict[str, Any]:
        data = {
            'mode': 'google',
            'id': self.id,
            'google_token': self.google_token,
            'google_uid': self.google_uid
        }
        return data
        
    def validate_user_data(self, data: dict[str, Any]) -> bool:
        return (data['mode'] == 'user' and 
                data['id'] == self.id and 
                data['username'] == self.username and 
                data['password_hash'] == self.password_hash)
        
    def generate_user_data(self) -> dict[str, Any]:
        data = {
            'mode': 'user',
            'id': self.id,
            'username': self.username,
            'password_hash': self.password_hash
        }
        return data
    
    def get_public_data(self) -> (dict[str, Any] | None):
        if not self.public_phone:
            return None
        data = {
            'about': self.about,
            'active': self.active,
            'address': self.address if self.public_address else None,
            'confirmed_at': self.confirmed_at,
            'creation': self.creation,
            'email': self.email if self.public_email else None,
            'image': self.image,
            'last_seen': self.last_seen,
            'phone': self.phone if self.public_phone else None
        }
        return data
    
    def get_private_data(self) -> dict[str, Any]:
        data = {
            'about': self.about, 
            'active': self.active, 
            'address': self.address, 
            'confirmed_at': self.confirmed_at, 
            'creation': self.creation, 
            'email': self.email, 
            'google_signin': self.google_signin, 
            'google_token': self.google_token, 
            'google_uid': self.google_uid, 
            'id': self.id, 
            'image': self.image, 
            'last_seen': self.last_seen, 
            'phone': self.phone, 
            'public_address': self.public_address, 
            'public_email': self.public_email, 
            'public_phone': self.public_phone, 
            'public_profile': self.public_profile, 
            'username': self.username
        }
        return data