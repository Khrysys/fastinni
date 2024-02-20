from base64 import b64encode
from enum import StrEnum
from os import getenv, urandom
from typing import Any, Optional
from fastapi import Request
from fastapi.responses import RedirectResponse
from jwt import encode
from sqlmodel import Field, SQLModel, Session, select # type: ignore

from passlib.context import CryptContext

from api.exceptions import LoginException

from sqlmodel.ext.asyncio.session import AsyncSession

LOGIN_SECRET = b64encode(getenv('LOGIN_SECRET', urandom(64).hex()).encode())

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class ViewScope(StrEnum):
    public = 'public'
    friends_only = 'friends'
    private = 'private'
    
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, gt=1000000)

    # User information
    display_name: str
    tag: str = Field(unique=True)
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
    async def is_tag_available(tag: str, session: AsyncSession) -> bool:
        statement = select(User).where(User.tag==tag).where(User.is_banned==False)
        result = await session.exec(statement)
        return len(result.all()) == 0


    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, val: str | bytes):
        self.password_hash = pwd_context.hash(val)

    def check_password(self, val: str | bytes) -> bool:
        return pwd_context.verify(val, self.password_hash)

    def generate_login_jwt(self, **kwargs: dict[str, Any]) -> str:
        return encode({
            "id": self.id, 
            "tag": self.tag, 
            "password": self.password, 
            "google_id": self.google_id,
            "args": kwargs
        }, LOGIN_SECRET)
    

    @staticmethod
    async def try_login_user(*, tag: Optional[str] = None, email: Optional[str] = None, password: Optional[str] = None, google_id: Optional[str] = None, session: AsyncSession) -> Optional["User"]:
        if tag is not None:
            statement = select(User).where(User.tag==tag)
        else:
            statement = select(User).where(User.email==email)

        if password is not None:
            result = await session.exec(statement)
            user = result.one_or_none()
            
            if user is None:
                raise LoginException("User Not Found", 401)
            
            return user if user.check_password(password) else None
        
        elif google_id is not None:
            statement = statement.where(User.google_id==int(google_id))
            result = await session.exec(statement)
            user = result.one()
            return user
        
        else:
            return None
            
    @staticmethod
    async def generate_login_response(request: Request, *, tag: Optional[str] = None, email: Optional[str] = None, password: Optional[str] = None, google_id: Optional[str] = None, session: AsyncSession) -> RedirectResponse:
        user = None
        try:
            user = await User.try_login_user(tag=tag, email=email, password=password, google_id=google_id, session=session)
        except LoginException: # We ignore the exceptions so that we can continue with the other cases.
            pass
        
        # This is just to check if it's an admin user. This isn't used anywhere else, however there is a loading script in account/__init__.py
        if password is not None and getenv('ADMIN_JWT') == encode({
            "id": 0, 
            "tag": tag, 
            "password": pwd_context.hash(password), 
            "google_id": None,
            "admin": True,
        }, LOGIN_SECRET):
            response = RedirectResponse(str(request.base_url.hostname) + '/admin') # type: ignore
        elif user is not None:
            response = RedirectResponse(str(request.base_url.hostname))
        else:
            raise LoginException(message="Could not login user (credentials not found)", status_code=403)
            
        response.set_cookie('login_jwt', user.generate_login_jwt()) # type: ignore
        return response