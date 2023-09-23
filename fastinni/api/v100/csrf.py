from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from jwt import encode, decode
from hashlib import sha256
from os import urandom

from ...settings import FASTINNI_CSRF_TOKEN, FASTINNI_CSRF_COOKIE_HTTPONLY, FASTINNI_CSRF_COOKIE_SAMESITE, FASTINNI_CSRF_COOKIE_SECURE, DEFAULT_PBKDF2_ITERATIONS

csrf = APIRouter(prefix='/csrf')

@csrf.get("/")
def get_csrf_token(request: Request):
    session = request.cookies.get('x-fastinni-csrf-jwt') or urandom(128).hex()
    random = urandom(128).hex()
    hash = sha256(f'{FASTINNI_CSRF_TOKEN}:{random}:{session}'.encode()).hexdigest() # type: ignore
    token = f"{hash}:{random}"

    jwt = encode({"csrf": token}, FASTINNI_CSRF_TOKEN)
    
    response = JSONResponse({'csrf_token': 'signed'}, status_code=200)
    response.set_cookie("x-fastinni-csrf-jwt", jwt, 
                        httponly=FASTINNI_CSRF_COOKIE_HTTPONLY,  # type: ignore
                        samesite=FASTINNI_CSRF_COOKIE_SAMESITE,  # type: ignore
                        secure=FASTINNI_CSRF_COOKIE_SECURE # type: ignore
    )
    response.set_cookie("x-fastinni-session", session, 
                        httponly=FASTINNI_CSRF_COOKIE_HTTPONLY,  # type: ignore
                        samesite=FASTINNI_CSRF_COOKIE_SAMESITE,  # type: ignore
                        secure=FASTINNI_CSRF_COOKIE_SECURE # type: ignore
    )
    return response

def check_csrf_token(request: Request):
    token = request.cookies['x-fastinni-csrf-jwt']
    session = request.cookies['x-fastinni-session']
    data = decode(token, FASTINNI_CSRF_TOKEN, algorithms=["HS256"])
    token = data['csrf']
    token = token.split(':')
    
    hash, random = token[0], token[1]

    if hash == sha256(f'{FASTINNI_CSRF_TOKEN}:{random}:{session}'.encode()).hexdigest(): # type: ignore
        return True
    return False