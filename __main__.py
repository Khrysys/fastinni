from asyncio import run
from os import getenv, path

from dotenv import load_dotenv
from uvicorn import Config, Server

load_dotenv()

from app import app, sqlalchemy as db

def update_db():
    run(db.create_all())
    if not path.exists('migrations'):
        db.migration.init() 
    db.migration.revision()
    db.migration.upgrade()

async def main():
    config = Config(app, host=getenv('HOST', '127.0.0.1'), port=int(getenv('PORT', '5000')), 
                    log_level="info", uds=getenv('UNIX_SOCKET', None), reload=True)
    server = Server(config)
    await server.serve()
    

if __name__ == '__main__':
    update_db()
    print('Database update complete')
    run(main())