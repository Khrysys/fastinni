from os import path, getenv
from uvicorn import Config, Server
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(debug=True, title="Fastinni")

from .extensions import csrf

async def run():
    # SSL Configuration if it exists
    if path.exists('./key.pem'):
        ssl_key = './key.pem'
    else:
        ssl_key = None
    if path.exists('./cert.pem'):
        ssl_cert = './cert.pem'
    else:
        ssl_cert = None
    
    config = Config(app, host=getenv('HOST', '127.0.0.1'), port=int(getenv('PORT', '5000')), 
                    log_level="info", uds=getenv('UNIX_SOCKET', None), reload=True,
                    ssl_keyfile=ssl_key, ssl_certfile=ssl_cert
                )
    server = Server(config)
    await server.serve()
    
app.mount(path='/', app=StaticFiles(directory='fastinni/pages', html=True), name='Pages')
from .api import api 
app.include_router(api, prefix="/api")