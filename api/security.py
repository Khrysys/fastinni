from os import getenv
from string import ascii_lowercase, digits
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_csrf_protect import CsrfProtect


app = APIRouter(prefix='/security', tags=['Security'])

@app.get('/csrf')
async def get_csrf_token(csrf_protect:CsrfProtect = Depends()):
	response = JSONResponse(status_code=200, content={'csrf_token':'cookie'})
	(_, token) = csrf_protect.generate_csrf_tokens()
	csrf_protect.set_csrf_cookie(token, response)
	return response

# This is thrown for values that are mentioned under OWasp's Input Validation cheat sheet that do not meet requirements.
# This should be caught anytime we are recieving a user input, which is pretty much everything.
# https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
class OWaspValidationException(Exception):
	pass

# Validates an email according to OWasp specifications.
# Throws OwaspValidationException when email is invalid.
def validate_email_address(email: str) -> None:
	# Check to make sure email has two parts separated by an @
	parts = email.split('@')
	if len(parts) is not 2:
		raise OWaspValidationException(f"Provided email {email} has {len(parts)} sections (required 2)")
	
	# Ensure email has no dangerous characters
	dangerous_characters = getenv("VALIDATION_EMAIL_DANGEROUS_CHARACTERS", '').split('') 
	for char in dangerous_characters:
		if char in email:
			raise OWaspValidationException(f"Provided email {email} contains dangerous character {char}")
		
	# Ensure that the domain section is valid
	domain_valid_characters = set(ascii_lowercase + digits + '-.')
	if not set(parts[1]).issubset(domain_valid_characters):
		raise OWaspValidationException(f"Provided email domain {parts[1]} contains illegal characters")
		
	# Validate the lengths
	if len(parts[0]) >= 64 or len(email) >= 255:
		raise OWaspValidationException(f"Provided email {email} is too long")

	