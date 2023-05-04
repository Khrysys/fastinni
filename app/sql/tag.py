from .. import sqlalchemy as db

class Tag(db.Model): # type: ignore
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return self.name