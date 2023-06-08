"""# This file contains all the endpoints referring to authentication methods.
# This includes the JWT, API Keys, OAuth, and anything else I come up with.
# This does not include CSRF Tokens or anything CORS related.
# The prefix for all routes in this file is "/auth"

from fastapi import Depends, Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_csrf_protect import CsrfProtect
from sqlmodel import Session, select

from .. import jwt, db
from ..routers import dev, latest
from ..sql import User
from ..security import check_password_hash, generate_password_hash

app = APIRouter(prefix='/auth', tags=['Authentication'])

@app.get('/jwt/check')
async def check_jwt_token(request: Request, csrf_protect: CsrfProtect = Depends()):
    csrf_protect.validate_csrf_in_cookies(request)
    '''
    Check the JWT token inside the cookie. 
    
    MAY RETURN:
        200, 400, 401, 403, 404, 500
    '''
    # Get JWT Data
    try:
        data = jwt.get_jwt_in_cookies(request)
    except:
        return JSONResponse({'detail': 'No JWT set'}, status_code=401)
    
    # this Try/except ensures every operation is valid
    try:
        signin_mode = data['mode']
    
        # Check if it is supposed to be a Google ID check
        match signin_mode:
            case 'GOOGLE':
                # Validate the token with Google
                id = data['id']
                google_token = data['google_token']
                token = data['token']
                with Session(db) as session:
                    user: User = session.exec(select(User).where(User.id==id).where(User.google_token==gid))
        
            # Check for signin using user credentials
            case 'USER':
                with Session(db) as session:
                    # Check against the database for the user credentials
                    id = data['id']
                    username = data['username']
                    password = data['pwhash']
                    user: User = session.exec(select(User).where(User.username==username).where(User.id==id)).one_or_none()
                    
                    if user.password_hash == password:
                        response = JSONResponse({'detail': 'JWT Accepted'}, status_code=200)
                        jwt.set_token_header(response, data)
                        return response
                    else:
                        response = JSONResponse({'detail': 'JWT incorrect'}, status_code=403)
                        jwt.set_token_header(response, None)
                        return response
            
            case _:
                jwt.set_token_header(response, None)
                response = JSONResponse({'detail': 'No Signin method found'}, status_code=403)
                return response
        
        
        #clear token and return 404
        response = JSONResponse({'detail': 'No user found with credentials'}, status_code=404)
        jwt.set_token_header(response, None)
        return response
    except:
        response = JSONResponse({'detail': 'Invalid JWT'}, status_code=403)
        jwt.set_token_header(response, None)
        return response
    
@app.post('/jwt/create')
async def add_jwt_token_cookie(request: Request, data: OAuth2PasswordRequestForm = Depends(), csrf_protect: CsrfProtect = Depends()):
    csrf_protect.validate_csrf_in_cookies(request)
    # Enssure JWT Data doesn't exist
    try:
        jwt.get_jwt_in_cookies(request)
        response = JSONResponse({'detail', 'JWT already set'}, status_code=202)
        return response
    except:
        pass
    
    # Build JWT data using form input
    name = data.username
    password = data.password
    try:
        with Session(db) as session:
            user: User = session.exec(select(User).where(User.username==name)).one_or_none()
            id = user.id
            pwhash = user.password_hash
            if not check_password_hash(user.password_hash, password):
                return JSONResponse({'detail': 'invalid credentials'}, 403)
    except:
        pwhash = generate_password_hash(password)
        user: User = User(
            username=name, 
            password_hash=pwhash
        )
        
        with Session(db) as session:
            session.add(user)
            session.commit()
            id = user.id
    
    jwt_data = {
        'mode': 'USER',
        'id': id,
        'username': name,
        'pwhash': pwhash,
    }
    response = JSONResponse({'detail': 'JWT cookie created'}, status_code=200)
    jwt.set_token_header(response, jwt_data)
    return response

from . import oauth
app.include_router(oauth.app)

dev.include_router(app)"""