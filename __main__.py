from uvicorn import Config, Server
from asyncio import run
from os import getenv
from dotenv import load_dotenv
load_dotenv()

async def main():
    config = Config('app:fastapi', port=5000, log_level="info")
    server = Server(config)
    await server.serve()

if __name__ == '__main__':
    run(main())