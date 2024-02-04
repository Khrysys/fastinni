from enum import StrEnum
from os import getenv
from typing import Optional
from jwt import encode
from sqlmodel import Field, SQLModel, Session, select

from passlib.context import CryptContext

from . import engine

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class ViewScope(StrEnum):
    public = 'public'
    related = 'related'
    friends = 'friends'
    private = 'private'
    

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)

    # User information
    display_name: str
    tag: str = Field(primary_key=True, unique=True)
    email: Optional[str] = Field(default=None, unique=True)
    # We are storing the URL of the profile image, since that allows for Google OAuth to work quite well.
    picture: str = Field(default='default_profile.jpg')

    # Possible login secret info that gets verified
    google_id: Optional[int] = Field(default=None)
    password_hash: Optional[str] = Field(default=None)

    # Toggles
    is_banned: Optional[bool] = Field(default=False)

    # View Modes
    profile_view: Optional[ViewScope] = Field(default=ViewScope.public)
    email_view: Optional[ViewScope] = Field(default=ViewScope.private)
    phone_view: Optional[ViewScope] = Field(default=ViewScope.private)
    integrations_view: Optional[ViewScope] = Field(default=ViewScope.private)

    @staticmethod
    def is_tag_available(tag: str) -> bool:
        with Session(engine) as session:
            statement = select(User).where(User.tag==tag).where(User.is_banned==False)
            result = session.exec(statement)
            return len(result.all()) == 0


    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, val):
        self.password_hash = pwd_context.hash(val)

    def check_password(self, val) -> bool:
        return pwd_context.verify(val, self.password_hash)

    def generate_login_jwt(self, **kwargs) -> str:
        return encode({
            "id": self.id, 
            "tag": self.tag, 
            "password": self.password, 
            "google_id": self.google_id,
            "args": kwargs
        }, getenv("LOGIN_SECRET")) # type: ignore
    

    @staticmethod
    def try_login_user(*, tag: Optional[str] = None, email: Optional[str] = None, password: Optional[str] = None, google_id: Optional[str] = None) -> Optional["User"]:
        with Session(engine) as session:
            if tag is not None:
                statement = select(User).where(User.tag==tag)
            else:
                statement = select(User).where(User.email==email)


            if password is not None:
                result = session.exec(statement)
                user: User = result.one()
                return user if user.check_password(password) else None
            
            elif google_id is not None:
                statement = statement.where(User.google_id==google_id)
                result = session.exec(statement)
                user: User = result.one()
                return user
            
            else:
                return None