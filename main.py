from fastapi import FastAPI
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
db = create_engine()

@app.get('/')
async def get_():
    return {'status': 'ok'}