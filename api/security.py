from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_csrf_protect import CsrfProtect


app = APIRouter(prefix='/security', tags=['Security'])

@app.get('/csrf')
async def get_csrf_token(csrf_protect:CsrfProtect = Depends()):
	response = JSONResponse(status_code=200, content={'csrf_token':'cookie'})
	csrf_protect.set_csrf_cookie(response) # type: ignore
	return response

