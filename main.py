from dotenv import load_dotenv
load_dotenv()

import asyncio
from os import system, path, getenv
from uvicorn import Config, Server
from fastinni import create_app
from fastinni.db import db

from alembic import command, config

async def migrate():
    async with db.begin() as session:
        cfg = config.Config("alembic.ini", attributes={'connection': session})
        if not path.exists("migrations"):
            command.init(cfg, 'migrations', template='async', package=True)


async def run():
    app = await create_app()
    await migrate()
    
    config = Config(app, host=getenv('FASTINNI_HOST', '127.0.0.1'), port=int(getenv('FASTINNI_PORT', '5000')), 
                    log_level="info", uds=getenv('FASTINNI_UNIX_SOCKET', None), reload=True,
                    ssl_keyfile=getenv("FASTINNI_SSL_KEYFILE"), ssl_certfile=getenv("FASTINNI_SSL_CERTFILE")
                )
    server = Server(config)
    await server.serve()

if __name__ == '__main__':
    code = system(f'npm run build && npm run pack')
    if code != 0:
        exit(code)
        
    asyncio.run(run())