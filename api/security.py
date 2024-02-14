from os import getenv
from string import ascii_lowercase, digits
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_csrf_protect import CsrfProtect

from .exceptions import OWaspValidationException


app = APIRouter(prefix='/security', tags=['Security'])

@app.get('/csrf')
async def get_csrf_token(csrf_protect:CsrfProtect = Depends()):
	response = JSONResponse(status_code=200, content={'csrf_token':'cookie'})
	(_, token) = csrf_protect.generate_csrf_tokens()
	csrf_protect.set_csrf_cookie(token, response)
	return response



# Validates an email according to OWasp specifications.
# Throws OwaspValidationException when email is invalid.
# Returns the inputted string again if it is valid.
def validate_email_address(email: str) -> str:
	'''
	Validates an email according to OWasp specifications.
	Throws OwaspValidationException when email is invalid.
	Returns the string again if it is valid.
	'''
	# Check to make sure email has two parts separated by an @
	parts = email.split('@')
	if len(parts) != 2:
		raise OWaspValidationException(message=f"Provided email {email} has {len(parts)} sections (required 2)")
	
	# Ensure email has no dangerous characters
	dangerous_characters = getenv("VALIDATION_EMAIL_DANGEROUS_CHARACTERS", '').split('') 
	for char in dangerous_characters:
		if char in email:
			raise OWaspValidationException(message=f"Provided email {email} contains dangerous character {char}")
		
	# Ensure that the domain section is valid
	domain_valid_characters = set(ascii_lowercase + digits + '-.')
	if not set(parts[1]).issubset(domain_valid_characters):
		raise OWaspValidationException(message=f"Provided email domain {parts[1]} contains illegal characters")
		
	# Validate the lengths
	if len(parts[0]) >= 64 or len(email) >= 255:
		raise OWaspValidationException(message=f"Provided email {email} is too long")
	

	return email

	