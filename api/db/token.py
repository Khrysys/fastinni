from enum import StrEnum
from secrets import choice
from string import ascii_letters, digits
from typing import Optional
from sqlmodel import Field
from sqlmodel import SQLModel

def gen_token():
    return ''.join(choice(ascii_letters + digits) for i in range(128))


class PossibleScopes(StrEnum):
    # All Public Data, this is normally requested by default and obeys the public view toggles
    user_public_read = 'user.public.read'
    user_public_write = 'user.public.write'
    # Only some private data, and this bypasses the public view toggles
    user_private_read = 'user.private.read'
    user_private_write = 'user.private.write'
    # This allows access to things like the google ID
    user_integrations_read = 'user.integrations.read'

    # Allows this token to manage other users and the app in general. 
    superuser_manage = 'user.super.manage'

class TokenType(StrEnum):
    bearer = 'bearer'
    authorization = 'authorizations'

class Token(SQLModel, table=True):
    token_type: TokenType
    access_token: Optional[str] = Field(default_factory=gen_token, unique=True)