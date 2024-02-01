from typing import Optional
from sqlmodel import Field, SQLModel, Session, select

from . import engine

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
        
    
    def generate_login_jwt(self) -> str:
        return ""
    
    def generate_oauth_jwt(self) -> str:
        return ""
        
    
            

