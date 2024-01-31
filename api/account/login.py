from fastapi import APIRouter, Depends, Request
from fastapi_csrf_protect import CsrfProtect


app = APIRouter(prefix='/login', tags=['Login'])

@app.get("/")
async def get_account_login_info():
    pass

@app.post('/')
async def attempt_account_login(request: Request, csrf_protect:CsrfProtect = Depends()):
    await csrf_protect.validate_csrf(request)
