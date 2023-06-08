from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from ..routers import dev
from fastapi import Body, Header
import json

app = APIRouter(prefix="/github")

async def update_pushed_repo(request: Request):
    body = await request.body()
    for s in body.decode().split('&'):
        print(s)

@app.post('/push')
async def post_github_push(request:Request):
    #print(request.headers)
    print("Github Pushed")
    await update_pushed_repo(request)
dev.include_router(app)