from dotenv import load_dotenv
load_dotenv()

import asyncio
from os import system, path, getenv
from uvicorn import Config, Server
from fastinni import create_app

app = create_app()

if __name__ == '__main__':
    code = system(f'npm install && npm run build && npm run pack')
    if code != 0:
        exit(code)
        
    config = Config(app, 
                    host=getenv('FASTINNI_HOST', '127.0.0.1'), 
                    port=int(getenv('FASTINNI_PORT', '5000')), 
                    log_level="info", 
                    uds=getenv('FASTINNI_UNIX_SOCKET', None), 
                    timeout_keep_alive=10,
                    ssl_keyfile=getenv("FASTINNI_SSL_KEYFILE"), 
                    ssl_certfile=getenv("FASTINNI_SSL_CERTFILE"),
                )
    server = Server(config)
    asyncio.run(server.serve())