from os import getenv
from fastapi import Cookie, Depends, HTTPException, Response
from typing import Annotated, Optional

from fastapi.requests import Request
from fastapi.routing import APIRouter
from pydantic import BaseModel
from sqlmodel import Session, select
from jwt import decode, encode
from .csrf import check_csrf_token
from ..db import engine
from ..db.user import User
from datetime import datetime

FASTINNI_LOGIN_SECRET = getenv("FASTINNI_LOGIN_SECRET", "secret")

account = APIRouter(prefix="/account", tags=["Account"])

class DetailResponse(BaseModel):
    detail: str

class PublicProfile(BaseModel):
    id: int
    name: str
    tag: str
    phone: Optional[str]
    email: Optional[str]
    address: Optional[str]
    about: str
    image: str
    active: bool
    confirmed_at: Optional[datetime]
    last_seen: Optional[datetime]

class GeneralInfo(BaseModel):
    id: int
    name: str
    tag: str
    image: str

responses = {
    403: {
        'description': 'Invalid CSRF Token',
        'model': DetailResponse,
        'content': {
            'application/json': {
                'example': {
                    'detail': 'Invalid CSRF Token'
                }
            }
        }
    }
}

@account.get('/user/{tag}',
    responses={
        **responses,
        404: {
            'description': 'User Not found',
            'model': DetailResponse,
            'content': {
                'application/json': {
                    'example': {
                        'detail': 'User "string" was not found'
                    }
                }
            }
        },
        204: {
            'description': 'Found Private Profile'
        },
        200: {
            'description': 'Found Public Profile',
            'model': PublicProfile,
            'content': {
                'application/json': {
                    'example': {
                        'id': 0,
                        'name': 'string',
                        'tag': 'string',
                        'phone': 'string',
                        'email': 'string',
                        'address': 'string',
                        'about': 'string',
                        'image': 'string',
                        'active': True,
                        'confirmed_at': None,
                        'last_seen': None
                    }
                }
            }
        }
    },
    response_model_include=None
)
def find_user_with_tag(tag: str, csrf_token: Annotated[str | None, Cookie()] = None, session: Annotated[str | None, Cookie()] = None):
    if not check_csrf_token(csrf_token, session):
        raise HTTPException(403, detail="Invalid CSRF Token")
    with Session(engine) as sess:
        try:
            user = sess.exec(select(User).where(User.tag==tag)).one()
            profile = user.get_profile()
            if not profile:
                return Response(status_code=204)
            return profile
        except:
            raise HTTPException(404, detail=f"The User @{tag} was not found")

@account.get('/user/{tag}/public',
    responses={
        **responses,
        404: {
            'description': "User Not Found",
            'model': DetailResponse,
            'content': {
                'application/json': {
                    'example': {
                        'detail': 'User "string" was not found'
                    }
                }
            }
        },
        200: {
            'description': 'Found User',
            'model': GeneralInfo,
            'content': {
                'application/json': {
                    'example': {
                        'id': 0,
                        'name': 'string',
                        'tag': 'string',
                        'image': 'string'
                    }
                }
            }
        }
    },
    response_model_include=None   
)
def get_general_user_info(tag: str, csrf_token: Annotated[str | None, Cookie()] = None, session: Annotated[str | None, Cookie()] = None):
    if not check_csrf_token(csrf_token, session):
        raise HTTPException(403, detail="Invalid CSRF Token")
    with Session(engine) as sess:
        try:
            user = sess.exec(select(User).where(User.tag==tag)).one()
            return {
                'id': user.id,
                'name': user.name,
                'tag': user.tag,
                'image': user.image
            }
        except:
            raise HTTPException(404, detail=f"The User @{tag} was not found")
        
@account.post('/login',
    responses={
        **responses,
        200: {
            'description': 'Logged in',
            'model': DetailResponse,
            'content': {
                'application/json': {
                    'example': {
                        'detail': 'Login Successful'
                    }
                }
            }
        }
    },
    response_model_include=None
)
def login(csrf_token: Annotated[str | None, Cookie()] = None, session: Annotated[str | None, Cookie()] = None):
    if not check_csrf_token(csrf_token, session):
        raise HTTPException(403, detail="Invalid CSRF Token")
    
    
@account.post('/signup')
def signup(csrf_token: Annotated[str | None, Cookie()] = None, session: Annotated[str | None, Cookie()] = None):
    if not check_csrf_token(csrf_token, session):
        raise HTTPException(403, detail="Invalid CSRF Token")
        
@account.get('/tag-available/{tag}')
def get_tag_availibility(tag: str, csrf_token: Annotated[str | None, Cookie()] = None, session: Annotated[str | None, Cookie()] = None):
    if not check_csrf_token(csrf_token, session):
        raise HTTPException(403, detail="Invalid CSRF Token")
    with Session(engine) as sess:
        try:
            sess.exec(select(User).where(User.tag==tag))
            return {}
        except:
            return {}
@account.get('/logout')
def logout(csrf_token: Annotated[str | None, Cookie()] = None, session: Annotated[str | None, Cookie()] = None):
    if not check_csrf_token(csrf_token, session):
        raise HTTPException(403, detail="Invalid CSRF Token")


@account.get("/get-data")
def get_current_user_data(
    login_jwt: Annotated[str | None, Cookie()] = None, 
    csrf_token: Annotated[str | None, Cookie()] = None, 
    session: Annotated[str | None, Cookie()] = None
):
    if not check_csrf_token(csrf_token, session):
        raise HTTPException(403, detail="Invalid CSRF Token")
    try:
        jwt = decode(login_jwt, FASTINNI_LOGIN_SECRET, algorithms=["HS256"]) # type: ignore

        with Session(engine) as sess:
            user = sess.exec(select(User).where(User.tag==jwt['tag']).where(User.name==jwt['username']).where(User.id==jwt['id'])).one()
            return {
                'username': user.name,
                'tag': user.tag,
                'email': user.email,
                'image': user.image
            }
    except:
        raise HTTPException(403, detail="Invalid Login JWT")