from fastapi import Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from fastapi_csrf_protect import CsrfProtect
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ...extensions import jwt
from ...sql import User, get_session, get_user

app = APIRouter(prefix='/jwt')

@app.get('/validate')
async def validate_jwt(request: Request, csrf: CsrfProtect = Depends(), dbsession: AsyncSession = Depends(get_session)):
    csrf.validate_csrf_in_cookies(request)
    # Find JWT
    try:
        data = jwt.get_jwt_in_cookies(request)
    except:
        return JSONResponse({'detail': 'JWT not found'}, status_code=401)
    
    user = await get_user(data, dbsession)
    if user is None:
        return JSONResponse({'JWT invalid'}, status_code=403)
    
    return JSONResponse({'detail': 'JWT Ok'}, status_code=200)
    
@app.get('/data')
async def get_private_user_data(request: Request, csrf: CsrfProtect = Depends(), dbsession: AsyncSession = Depends(get_session)):
    csrf.validate_csrf_in_cookies(request)
    
    try: 
        data = jwt.get_jwt_in_cookies(request)
    except:
        return JSONResponse({'detail': 'JWT not found'}, status_code=401)
    
    user = await get_user(data, dbsession)
    if user is None:
        return JSONResponse({'JWT invalid'}, status_code=403)
    
    return JSONResponse(user.get_private_data(), status_code=200)

@app.post('/new')
async def create_new_user(request: Request, csrf: CsrfProtect = Depends(), dbsession: AsyncSession = Depends(get_session)):
    pass