from json import dumps

from authlib.integrations.starlette_client import OAuthError
from fastapi import Depends, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.routing import APIRouter
from fastapi_csrf_protect import CsrfProtect
from requests import get, post
from sqlmodel import Session, select

from ... import db, jwt, oauth
from ...config import (GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,
                       get_google_provider_cfg)
from ...sql import User

app = APIRouter(prefix='/google')

@app.get('/')
def google_oauth(request: Request, csrf: CsrfProtect = Depends()):
    csrf.validate_csrf_in_cookies(request)
    
    authorization_endpoint = "https://accounts.google.com/o/oauth2/v2/auth"
    request_uri = oauth.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.url_for('callback'),
        scope=["openid", "email", "profile"],
    )
    return RedirectResponse(request_uri)
'''
@app.get('/callback')
def google_oauth_callback(request: Request, csrf: CsrfProtect = Depends()):
    #csrf.validate_csrf_in_cookies(request)
    print(request.url)
    print(f"{request.base_url}{request.url.path[1:]}")
    
    code = request.query_params.get('code')
    token_endpoint = "https://oauth2.googleapis.com/token"
    
    token_url, headers, body = oauth.prepare_token_request(
        token_endpoint,
        authorization_response=f"{request.url}",
        redirect_url=f"{request.base_url}{request.url.path[1:]}",
        code=code
    )
    
    token_response = post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    if token_response.status_code != 200:
        return JSONResponse({'detail': f'OpenID POST {token_url} failed with {token_response.status_code}'}, token_response.status_code)
    oauth.parse_request_body_response(dumps(token_response.json()))
    
    userinfo_endpoint = "https://openidconnect.googleapis.com/v1/userinfo"
    uri, headers, body = oauth.add_token(userinfo_endpoint)
    userinfo_response = get(uri, headers=headers, data=body)
    
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return RedirectResponse('../../../account/login_failed')
    
    with Session(db) as session:
        user: User = session.exec(select(User).filter_by(google_token=unique_id))
        if user is not None:
            data = {
                'mode': 'GOOGLE',
                'id': user.id,
                'google_token': user.google_token,
            }
            
        else:
            user: User = User(
                username = users_name,
                email = users_email,
                image = picture,
                google_signin=True,
                google_token=unique_id
            )
            session.add(user)
            data = {
                'mode': 'GOOGLE',
                'id': user.id,
                'google_token': user.google_token,
            }
            
            session.commit()
            
        response = JSONResponse({'detail': 'Ok'}, status_code=200)
        jwt.set_token_header(response, data)
        return response
        '''
        
@app.get('/')
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
async def callback(request: Request):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        return JSONResponse({'detail': 'OAuthError'}, status_code=400)
    user_data = dict(await oauth.google.parse_id_token(request, access_token))
    
    with Session(db) as session:
        user: User | None = session.exec(select(User).where()).one_or_none()
        if user is None:
            user = User(
                username = 
            )
        
    
    response = JSONResponse({'detail':'Oauth OK'}, status_code=200)
    return 
