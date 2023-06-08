from fastapi import APIRouter

app = APIRouter(prefix='/v1', tags=['Version 1.0.0'])

from . import csrf, auth, github

app.include_router(auth.app)
app.include_router(csrf.app)
app.include_router(github.app)