from os import getenv, urandom
from secrets import choice
from string import ascii_lowercase, digits
from typing import Annotated
from fastapi import APIRouter, Cookie, Header
from fastapi.responses import JSONResponse
from hashlib import sha256

from jwt import PyJWTError, decode, encode

from .exceptions import CSRFValidationException, OWaspValidationException


CSRF_TOKEN = getenv("CSRF_TOKEN", urandom(64).hex())
ALGORITHMS = ['HS256']

app = APIRouter(prefix='/security', tags=['Security'])

@app.get('/csrf')
async def get_csrf_token():
	response = JSONResponse(status_code=200, content={'csrf_token':'cookie'})
	token = sha256(urandom(64)).hexdigest()
	data = encode({"token": token}, CSRF_TOKEN, choice(ALGORITHMS))
	response.set_cookie('csrf', data)
	return response

async def check_csrf_token(data: Annotated[str, Header(alias='X-CSRF-Token')], check: Annotated[str, Cookie(alias='csrf')]) -> bool:
	try:
		token = decode(data, CSRF_TOKEN, ALGORITHMS).get('token')
		check_token = decode(check, CSRF_TOKEN, ALGORITHMS).get('token')
		if token is None or check_token is None:
			raise CSRFValidationException("Tokens must exist")
		
		if token != check_token:
			raise CSRFValidationException("Tokens do not match")

		return True
	except PyJWTError:
		raise CSRFValidationException("Invalid Signature")
		
		

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