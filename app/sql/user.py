from datetime import datetime
import uuid

from .. import sqlalchemy as db
from .. import login
from .tables import roles_users

def uuid_generator():
    return uuid.uuid4().hex

class User(db.Model): # type: ignore
    __tablename__ = 'user'
    # Our User has six fields: ID, email, password, active, confirmed_at and roles. The roles field represents a
    # many-to-many relationship using the roles_users table. Each user may have no role, one role, or multiple roles.
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(155))
    last_name = db.Column(db.String(155))
    phone = db.Column(db.String(20))
    """While there are many ways to store phone numbers, here a string is being used."""
    address = db.Column(db.Text)
    about = db.Column(db.Text)
    image = db.Column(db.String(125))
    """Name of file that's kept in the user's folder"""
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False, default=uuid_generator)
    """This property is required by Flask-Security-Too"""
    # TOGGLES
    active = db.Column(db.Boolean(), default=True)
    public_profile = db.Column(db.Boolean(), default=True)
    # DATES
    confirmed_at = db.Column(db.DateTime())
    last_seen = db.Column(db.DateTime(), default=None)
    """This property is automatically updated in the `before_request` function as defined in the app's `__init__.py` file."""
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    
    roles = db.relationship(
        'User', secondary=roles_users, backref='role_id'
    )
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
        
