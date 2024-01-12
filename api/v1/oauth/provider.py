from datetime import datetime, timedelta, timezone
from os import getenv
from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException, Header, Request, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import RequestValidationError
from jwt import decode, encode
from oauthlib.oauth2 import WebApplicationServer
from sqlmodel import Session, select

from ...db import engine, User, AccessClient, BearerToken

app = APIRouter(prefix='/endpoints', tags=['Authorization'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
   user = await User.validate_jwt(token)
   if User is None:
       raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
   
   return user

@app.get('/')
def begin_oauth_check(request: Request, x_fastinni_csrf: Annotated[str | None, Header()] = None):
    if x_fastinni_csrf is None or decode(x_fastinni_csrf, getenv("LOGIN_SECRET"), algorithms=["HS256"]) is None: # type: ignore
        return Response({"response": "Invalid CSRF JWT"}, status_code=403)
    
    uri = request.base_url
    http_method = uri.scheme
    body = uri.query
    headers = request.headers

@app.post('/token')
def get_bearer_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    with Session(engine) as session:
        statement = select(User).where(User.id==form_data.client_id).where(User.username==form_data.username)
        result = session.exec(statement)
        user: User = result.one_or_none() # type: ignore

        if not user:
            raise HTTPException(status_code=403, detail="Incorrect username or password")

    data = {
        'access_token': token.access_token,
        'client_id': token.client_id,
        'user_id': token.user_id,
    }
        
