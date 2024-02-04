from fastapi import APIRouter, Depends, Request
from fastapi_csrf_protect import CsrfProtect


app = APIRouter(prefix='/login', tags=['Login'])

@app.get("/")
# If additional form security is required it should be put here, additionally request and browser verification
# should be verified here
async def get_account_login_info(request: Request):
    # We don't want two accounts to be logged in (although this can be done by adjusting the JWT styles)
    if request.cookies.get('login_jwt') is not None:
        return 400

@app.post('/')
async def attempt_account_login(request: Request, csrf_protect:CsrfProtect = Depends()):
    await csrf_protect.validate_csrf(request)
    
    tag = request.get('tag')
    password = request.get('password')



