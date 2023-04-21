from asyncio import run
from os import getenv

from dotenv import load_dotenv
from uvicorn import Config, Server

load_dotenv()

async def main():
    from app import fastapi
    config = Config(fastapi, port=getenv('PORT', 5000), log_level="info", root_path='/api', uds=getenv('UNIX_SOCKET', None), reload=True)
    server = Server(config)
    await server.serve()

if __name__ == '__main__':
    run(main())