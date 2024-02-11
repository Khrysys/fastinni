from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi_csrf_protect.exceptions import CsrfProtectError

from .security import OWaspValidationException

from . import api

@api.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
	return JSONResponse(content={ 'detail':  exc.message }, status_code=exc.status_code)

@api.exception_handler(OWaspValidationException)
def owasp_validation_exception_handler(request: Request, exc: OWaspValidationException):
	return JSONResponse(content={'detail': str(exc)}, status_code=400)