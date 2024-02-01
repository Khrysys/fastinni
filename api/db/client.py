from enum import StrEnum
from secrets import choice
from string import ascii_letters, digits
from typing import List, Optional
from sqlmodel import Field, SQLModel

class PossibleScopes(StrEnum):
    # All Public Data, this is normally requested by default and obeys the public view toggles
    user_public_read = 'user.public.read'
    user_public_write = 'user.public.write'
    # Only some private data, and this bypasses the public view toggles
    user_private_read = 'user.private.read'
    user_private_write = 'user.private.write'
    # This allows access to things like the google ID
    user_integrations_read = 'dangerous.user.integrations.read'
    user_integrations_write = 'dangerous.user.integrations.write'

    # Allows this token to manage other users and the app in general. 
    superuser_manage = 'user.super.manage'


def gen_secret() -> str:
    return ''.join(choice(ascii_letters + digits) for i in range(128))

class Client(SQLModel, table=True):
    # For clients, the ID is hashed so that we can add more security before it is given to the developer.
    id: Optional[int] = Field(primary_key=True)

    # This is the highest security value in this table, the client secret. Make sure that it is secure from just about everything before we share this to a dev.
    secret: str = Field(default_factory=gen_secret)

    # Holds a list of the scopes that this client is requesting to use. if any scopes have the keyword dangerous
    scopes: List[PossibleScopes]

    # Just some things to remember in case this client has been banned from other places
    developer_name: str
    developer_email: str
    app_name: str

    
