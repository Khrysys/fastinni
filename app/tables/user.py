from sqlalchemy import Table, Column, Integer, Text, DateTime
from datetime import datetime

from .. import db_metadata

user_table = Table(
    'user_table',
    db_metadata,
    Column('id', Integer, primary_key=True),
    
    Column('username', Text, nullable=False),
    Column('password_hash', Text, nullable=False),
    
    Column('creation', DateTime, nullable=False, default=datetime.utcnow())
)