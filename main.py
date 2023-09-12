import asyncio
from os import getenv, path

from dotenv import load_dotenv
from uvicorn import Config, Server
from os import path, getcwd, system

load_dotenv()

if __name__ == '__main__':
    code = system(f'npm run build && npm run pack')
    if code != 0:
        exit(code)
        
    from fastinni import run
    asyncio.run(run())