from json import dumps

from authlib.integrations.starlette_client import OAuthError
from fastapi import Depends, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.routing import APIRouter
from fastapi_csrf_protect import CsrfProtect
from requests import get, post
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ... import db, jwt, oauth
from ...config import (GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,
                       get_google_provider_cfg)
from ...sql import User, get_session

app = APIRouter(prefix='/google')

@app.get('/', status_code=200)
@slowapi.limiter
async def login(request: Request, csrf: CsrfProtect = Depends()):
    csrf.validate_csrf_in_cookies(request)
    try:
        data = jwt.get_jwt_in_cookies(request)
        return RedirectResponse(f"{request.base_url}v1/auth/jwt/check")
    except:
        pass
    
    redirect_uri = request.url_for('callback')  # This creates the url for the /auth endpoint
    return await oauth.google.authorize_redirect(request, str(redirect_uri))

@app.get('/callback')
async def callback(request: Request, csrf: CsrfProtect = Depends(), session: AsyncSession = Depends(get_session)):
    csrf.validate_csrf_in_cookies(request)
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        return JSONResponse({'detail': 'OAuthError'}, status_code=400)
    user_data = await oauth.google.parse_id_token(request, access_token)
    user_data = dict(user_data)
    
    user: User | None = session.execute(select(User).where()).one_or_none()
    if user is None:
        user = User(
            username = user_data['given_name'],
            google_signin=True
        )
    else:
        
        
    
    response = JSONResponse({'detail':'Oauth OK'}, status_code=200)
    return 
