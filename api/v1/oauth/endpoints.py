from os import getenv
from typing import Annotated
from fastapi import APIRouter, Header, Request, Response
from jwt import decode
from oauthlib.oauth2 import WebApplicationServer
from .request_validator import RequestValidator

server = WebApplicationServer(RequestValidator)

app = APIRouter(prefix='/endpoints', tags=['Authorization'])

@app.get('/')
def begin_oauth_check( request: Request, x_fastinni_csrf: Annotated[str | None, Header()] = None):
    if x_fastinni_csrf is None or decode(x_fastinni_csrf, getenv("LOGIN_SECRET"), algorithms=["HS256"]) is None: # type: ignore
        return Response({"response": "Invalid CSRF JWT"}, status_code=403)
    
    uri = request.base_url
    http_method = uri.scheme
    body = uri.query
    headers = request.headers
