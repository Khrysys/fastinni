from . import Base
from sqlalchemy import Column, String
from fastapi.responses import JSONResponse

class User(Base):
    # This user has six main fields: the ID (Comes from Base), username, email, is_active, confirmed_at, and roles. 
    # These are the identifiers primarily used, and the rest are general profile info that is not regularly seen.
    
    __tablename__ = "__users__"
    username = Column("username", String, nullable=False, unique=False)
    tag = Column("tag", String, nullable=False, unique=True)
    
    password_hash = Column("password", String)
    
    is_public = Column("is_public")
    
    first_name = Column(String(155))
    last_name = Column(String(155))
    phone = Column(String(20))
    
    @staticmethod
    def get_profile(user):
        if not user.is_public:
            return JSONResponse({user.tag: "Profile is Private"}, status_code=403)
        return JSONResponse({
            user.tag: {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone": user.phone
            }
        })