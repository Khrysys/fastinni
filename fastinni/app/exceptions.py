from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi_csrf_protect.exceptions import (CsrfProtectError,
                                             InvalidHeaderError,
                                             MissingTokenError,
                                             TokenValidationError)

from .extensions import app

@app.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
    return JSONResponse(status_code=exc.status_code, content={ 'detail':  exc.message, 'endpoint': f"{request.url}"})

@app.exception_handler(InvalidHeaderError)
def invalid_header_exception_handler(request: Request, exc: InvalidHeaderError):
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.message, 'endpoint': f'{request.url}'})

@app.exception_handler(MissingTokenError)
def missing_token_exception_handler(request: Request, exc: MissingTokenError):
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.message, 'endpoint': f'{request.url}'})

@app.exception_handler(TokenValidationError)
def token_validation_exception_handler(request: Request, exc: TokenValidationError):
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.message, 'endpoint': f'{request.url}'})