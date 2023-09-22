from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, Session, SQLModel, select, UniqueConstraint
from .roles_users import RolesUsers
from .roles import Role

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)

    name: Optional[str]
    tag: str = Field(unique=True)

    phone: Optional[str] = Field(unique=True)
    email: Optional[str] = Field(unique=True)
    address: Optional[str]
    about: Optional[str]
    image: Optional[str]
    password_hash: Optional[str]

    active: Optional[bool] = Field(default=True)
    public_profile: Optional[bool] = Field(default=True)

    confirmed_at: Optional[datetime]
    last_seen: Optional[datetime]

    roles: List[Role] = Relationship(back_populates="users", link_model=RolesUsers)

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
            