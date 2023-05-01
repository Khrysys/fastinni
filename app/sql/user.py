from datetime import datetime

from .. import sqlalchemy as db
from .. import login

class User(db.Model): # type: ignore
    __tablename__ = '__user_table__'
    id =            db.Column('id',            db.Integer,     primary_key=True, nullable=False)
    username =      db.Column('username',      db.Text,        nullable=False, unique=True)
    password_hash = db.Column('password_hash', db.Text,        nullable=False)
    creation =      db.Column('creation',      db.DateTime,    nullable=False, default=datetime.utcnow())

    def __str__(self):
        return 'User <{}, {}>'.format(self.id, self.username)
    
    def get_data(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'creation': self.creation,
        }
   
@login.user_loader()  # type: ignore
async def query_user(user_id: str) -> User:
    r = await db.session.execute(db.select(User).filter_by(username=user_id)) # type: ignore
    r = r.scalar_one()
    return r
        
