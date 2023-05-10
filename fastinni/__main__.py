from asyncio import run
from os import getenv, path

from dotenv import load_dotenv
from uvicorn import Config, Server
from os import path

load_dotenv()

from app import app

async def main():
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
    

if __name__ == '__main__':
    run(main())