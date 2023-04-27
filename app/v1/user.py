from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_csrf_protect import CsrfProtect
from fastapi_login.exceptions import InvalidCredentialsException

from .. import login, sqlalchemy as db
from ..routers import dev, latest
from ..security import check_password_hash, generate_password_hash
from ..sql.user import User, query_user
from . import v1 as app


@dev.get('/user/info/{username}')
@latest.get('/user/info/{username}')
@app.get('/user/info/{username}')
async def get_user_with_username(username: str):
    user = await query_user(username)
    
    if not user:
        raise HTTPException(status_code=404, detail='UID{} does not exist')
    return repr(user)

@dev.get('/user/login')
@latest.get('/user/login')
@app.get('/user/login')
async def get_user_login(request: Request, data: OAuth2PasswordRequestForm = Depends(), csrf: CsrfProtect = Depends()):
    csrf.validate_csrf_in_cookies(request)
    username = data.username
    password = data.password
    
    user = await query_user(username)
    if not user:
        raise InvalidCredentialsException
    elif not check_password_hash(user.password_hash, password): # type: ignore
        raise InvalidCredentialsException
    
    access_token = login.create_access_token(
        data={'sub': username}
    )
    return {'access_token': access_token}

@dev.post('/user/create')
@latest.post('/user/create')
@app.post('/user/create')
async def post_user_create(request: Request, data: OAuth2PasswordRequestForm = Depends(), csrf: CsrfProtect = Depends()):
    csrf.validate_csrf_in_cookies(request)
    username = data.username
    password = data.password
    
    user = User(username=username, password_hash=generate_password_hash(password))
    r = repr(user)
    db.session.add(user)
    await db.session.commit()
    return r