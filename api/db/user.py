from os import getenv
from typing import Optional
from jwt import encode
from sqlmodel import Field, SQLModel, Session, select

from passlib.context import CryptContext

from . import engine

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    is_banned: Optional[bool] = Field(default=False)

    display_name: str

    tag: str

    @staticmethod
    def is_tag_available(tag: str) -> bool:
        with Session(engine) as session:
            statement = select(User).where(User.tag==tag).where(User.is_banned==False)
            result = session.exec(statement)
            return len(result.all()) is 0

    password_hash: Optional[str]

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, val):
        self.password_hash = pwd_context.hash(val)

    def check_password(self, val) -> bool:
        return pwd_context.verify(val, self.password_hash)

    
    google_id: Optional[int]

    def generate_login_jwt(self, **kwargs) -> str:
        return encode({
            "id": self.id, 
            "tag": self.tag, 
            "password": self.password, 
            "google_id": self.google_id,
            "args": kwargs
        }, getenv("LOGIN_SECRET")) # type: ignore
        
    
            

