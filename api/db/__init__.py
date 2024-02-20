from os import getenv
from sqlmodel import SQLModel, create_engine

from .user import User # type: ignore

from os import getenv, path
from subprocess import run
from typing import Optional
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from typer import Typer

_app: Typer = Typer()

class SQLModelAlembic():
    _engine: AsyncEngine
    
    def __init__(self, db_url: str):
        self._engine = AsyncEngine(create_engine(db_url, echo=True, future=True))
        self._sessionmaker = sessionmaker(
            bind=self._engine, class_=AsyncSession, expire_on_commit=False # type: ignore
        )
    
    async def init(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
            
    async def __call__(self):
        return self.get_session()
        
            
    async def get_session(self) -> AsyncSession: # type: ignore
        async with self._sessionmaker() as session: # type: ignore
            yield session # type: ignore
       
    @staticmethod     
    @_app.command()
    def db_init(path_to_db: str, directory: str = 'migrations', db_url: Optional[str] = None, db_env_var: str = 'DB_URL'):
        if path.exists(directory):
            print('FAILED: Directory migrations already exists and is not empty')
            exit(1)
            
        run(['alembic', 'init', '-t', 'async', directory])
        
        with open(f'{directory}/script.py.mako', 'r') as f:
            data = f.read()
            
        # Find the part of the file that has a SQLAlchemy import and add a SQLModel import
        insert = 'import sqlalchemy as sa'
        index = data.index(insert) + len(insert)
        new_data = data[:index] + '\nimport sqlmodel' + data[index:]
        
        with open(f'{directory}/script.py.mako', 'w') as f:
            f.write(new_data)
            
        with open(f'{directory}/env.py', 'r') as f:
            data = f.read()
            
        db_path = path_to_db.replace('/', '.').replace('\\', '.')
        insert = 'from sqlalchemy.ext.asyncio import async_engine_from_config'
        index = data.index(insert) + len(insert)
        new_data = f'{data[:index]}\nfrom sqlmodel import SQLModel\n\nimport {db_path}\n\n{data[index:]}'
        
        # Replace this
        insert = 'target_metadata = None'
        index = new_data.index(insert)
        new_data = f'{new_data[:index]}target_metadata = SQLModel.metadata{new_data[index+len(insert):]}'
        
        with open(f'{directory}/env.py', 'w') as f:
            f.write(new_data)
            
        with open(f'alembic.ini', 'r') as f:
            data = f.read()
            
        # Replace this
        insert = 'script_location = migrations'
        index = data.index(insert)
        new_data = f'{data[:index]}script_location = {directory}{data[index+len(insert):]}'
        
        # Replace this
        insert = 'sqlalchemy.url = driver://user:pass@localhost/dbname'
        index = new_data.index(insert)
        new_data = f'{new_data[:index]}sqlalchemy.url = {db_url or getenv(db_env_var)}{new_data[index+len(insert):]}'
        
        with open(f'alembic.ini', 'w') as f:
            f.write(new_data)
    
    @staticmethod
    @_app.command()
    def db_upgrade(message: str):
        run(['alembic', 'revision', '--autogenerate', '-m', message])
        run(['alembic', 'upgrade', 'head'])
    
db = SQLModelAlembic(getenv('DB_URL')) # type: ignore