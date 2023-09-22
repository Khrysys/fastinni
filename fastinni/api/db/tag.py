from typing import Optional, List


from sqlmodel import SQLModel, Relationship, Field

class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)