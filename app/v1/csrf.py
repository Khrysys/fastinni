from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi_csrf_protect import CsrfProtect

from . import v1 as app


@app.get("/csrftoken")
async def get_csrf_token(csrf_protect:CsrfProtect = Depends()):
	response = JSONResponse(status_code=200, content={'csrf_token':'cookie'})
	csrf_protect.set_csrf_cookie(response)
	return response