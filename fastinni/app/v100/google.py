
from json import dumps

from fastapi import Depends, Request
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi_csrf_protect import CsrfProtect
from requests import get, post

from ..config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, get_google_provider_cfg
from ..routers import dev, latest
from . import v100 as app
from ..sql.user import User
from .. import sqlalchemy as db, jwt, oauth

@app.get('google/oauth/callback')
@dev.get('google/oauth/callback')
@latest.get('google/oauth/callback')
def google_oauth_callback(request: Request, csrf: CsrfProtect = Depends()):
    csrf.validate_csrf_in_cookies(request)
    
    code = request.data
    
    token_endpoint = get_google_provider_cfg()["token_endpoint"]
    
    token_url, headers, body = oauth.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    
    token_response = post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    
    
    oauth.parse_request_body_response(dumps(token_response.json()))
    
    userinfo_endpoint = get_google_provider_cfg()["userinfo_endpoint"]
    uri, headers, body = oauth.add_token(userinfo_endpoint)
    userinfo_response = get(uri, headers=headers, data=body)
    
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return RedirectResponse('../../../account/login_failed')

    user: User = db.session.execute(db.select(User).filter_by(gid=unique_id))
    if user is not None:
        data = {
            'path': request.url,
            'id': user.id,
            'gid': unique_id,
            'username': user.username,
            'email': users_email
        }