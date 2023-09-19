from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from starlette.routing import BaseRoute
from fastapi import Depends
from fastapi_csrf_protect import CsrfProtect


csrf = APIRouter(prefix="/csrf")

@csrf.get("/token", responses={200: {"csrf_token": 'cookie'}, 404: {"detail": "not found"}})
async def get_csrf_token(csrf_protect: CsrfProtect = Depends()):
    (token, signed) = csrf_protect.generate_csrf_tokens()
    response = JSONResponse(status_code=200, content={'csrf_token': signed})
    csrf_protect.set_csrf_cookie(csrf_signed_token=signed, response=response)
    return response
