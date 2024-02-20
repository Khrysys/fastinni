from fastapi import Request
from fastapi.responses import JSONResponse

from . import api

class BaseException(Exception):
	'''
	This is a basic Exception that should be thrown for all errors that are not supposed to be caught, but instead 
	should generate a JSONResponse object. This allows for FastAPI's OpenAPI descriptors to figure things out properly.
	All other non-caught exceptions should inherit from this.
	These sub-exceptions are caught inside of `exceptions.py`.
	'''
	def __init__(self, message: str, status_code: int = 400):
		self.message = message
		self.status_code = status_code
	message: str
	status_code: int = 400

class OWaspValidationException(BaseException):
	'''
	This is thrown for values that are mentioned under OWasp's Input Validation cheat sheet that do not meet requirements.
	https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
	'''
	 
class CSRFValidationException(BaseException):
    '''
    This is thrown in a case where the CSRF token is somehow incorrect. The general rules for CSRF is following a double submit cookie pattern, and also uses a custom header as the "submitted" value. 
    Remember that if you add an XSS hole somewhere, CSRF does NOT protect you whatsoever in the case of an XSS attack. XSS beats CSRF. 
    https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
    '''
    status_code = 401

# This is thrown anytime that there is an issue with logging in. Pretty simple, and it keeps FastAPI happy with the responses being simple.
class LoginException(BaseException):
	'''
	This is thrown anytime that there is an issue with logging in. Pretty simple, and it keeps FastAPI happy with the responses being simple.
	This can also have subclassed errors for more fine grained control over what the issue is.
	'''

@api.exception_handler(BaseException)
def owasp_validation_exception_handler(request: Request, exc: BaseException):
	return JSONResponse(content={ 'detail': exc.message, 'url': str(request.url), 'type': str(exc.__class__)}, status_code=exc.status_code)