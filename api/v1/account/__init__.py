from typing import Annotated, Dict
from fastapi import APIRouter, Header, Response
from os import getenv
from datetime import datetime, timedelta
from jwt import encode, decode
from time import mktime

from pydantic import BaseModel

app = APIRouter(prefix='/account', tags=['Account'])

@app.get('/login')
def get_login_header_info() -> Dict[str, str]:
    secret = getenv("LOGIN_SECRET", "")
    date = datetime.utcnow() + timedelta(minutes=15)
    encoded = encode({'nbf': mktime(datetime.utcnow().timetuple()), 'exp': mktime(date.timetuple())}, secret, algorithm="HS256")

    # Return the name of the header, and the jwt that should go inside of the header data
    return {"name": "X_FASTINNI_CSRF", "data": encoded}

@app.post('/login')
def try_login(data: str | bytes, x_fastinni_csrf: Annotated[str | None, Header()] = None):
    secret = getenv("LOGIN_SECRET", "")

    if x_fastinni_csrf is None or decode(x_fastinni_csrf, secret, algorithms=["HS256"]) is None:
        return Response({"response": "Invalid CSRF JWT"}, status_code=403)

    print("Logging In")