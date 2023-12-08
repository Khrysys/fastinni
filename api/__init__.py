from fastapi import FastAPI

app = FastAPI(title="Fastinni", docs_url='/docs', redoc_url=None)

from .v1 import app as v1
app.include_router(v1)
from .routers import latest, dev
app.include_router(latest)
app.include_router(dev)