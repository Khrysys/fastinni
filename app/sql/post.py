from datetime import datetime
import humanize

from .tables import tags_posts
from .. import sqlalchemy as db

class Post(db.Model): # type: ignore
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80))
    subtitle = db.Column(db.String(80))
    body = db.Column(db.Text) 
    image = db.Column(db.String(125))
    """The name of the file that will be placed in `static/uploads/blog/`"""
    slug = db.Column(db.String(125), unique=True)
    publish_date = db.Column(db.DateTime(), default=datetime.utcnow)
    live = db.Column(db.Boolean)
    tags = db.relationship(
        'Tag',
        secondary=tags_posts,
        backref='posts'
    )
      
    @property
    def pubdate(self):
        """Return the date in readable English """
        return humanize.naturaltime(self.publish_date) # type: ignore

    def __repr__(self):
        if self.title:
            return f'<Post {self.title}>'
        else: return super().__repr__()