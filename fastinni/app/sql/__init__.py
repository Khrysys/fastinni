from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from ..config import SQLALCHEMY_DATABASE_URI
from ..extensions import db
from .links import RolesUsers, TagsPosts
from .post import Post
from .role import Role
from .tag import Tag
from .user import User


async def init_db():
    async with db.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        db, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
        
async def get_user(data: dict[str, Any], dbsession: AsyncSession):
    try:
        user = await dbsession.execute(select(User).where(User.id==id))
        if user is None:
            return None
        match data['mode']:
            case 'google':
                valid = user.validate_google_data(data)
            case 'user':
                valid = user.validate_user_data(data)
            case _:
                return None
        if valid is False:
            return None
        return user
                
    except:
        return None