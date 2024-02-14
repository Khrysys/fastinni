from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi_csrf_protect.exceptions import CsrfProtectError

from . import api

class BaseException(Exception):
	def __init__(self, message: str, status_code: int = 400):
		self.message = message
		self.status_code = status_code
	'''
	This is a basic Exception that should be thrown for all errors that are not supposed to be caught, but instead 
	should generate a JSONResponse object. This allows for FastAPI's OpenAPI descriptors to figure things out properly.
	All other non-caught exceptions should inherit from this.
	'''
	message: str
	status_code: int = 400

class OWaspValidationException(BaseException):
	'''
	This is thrown for values that are mentioned under OWasp's Input Validation cheat sheet that do not meet requirements.
	This is automatically caught by an exception handler in `exceptions.py`.
	https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
	'''
	

# This is thrown anytime that there is an issue with logging in. Pretty simple, and it keeps FastAPI happy with the responses being simple.
class LoginException(BaseException):
	'''
	This is thrown anytime that there is an issue with logging in. Pretty simple, and it keeps FastAPI happy with the responses being simple.
	'''

@api.exception_handler(LoginException)
def login_exception_handler(request: Request, exc: LoginException):
	return JSONResponse(content={ 'detail': exc.message, 'url': str(request.base_url) }, status_code=exc.status_code)

@api.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
	return JSONResponse(content={ 'detail': exc.message, 'url': str(request.base_url) }, status_code=exc.status_code)

@api.exception_handler(OWaspValidationException)
def owasp_validation_exception_handler(request: Request, exc: OWaspValidationException):
	return JSONResponse(content={ 'detail': exc.message, 'url': str(request.base_url) }, status_code=exc.status_code)