from fastapi import FastAPI, Request
from fastapi.middleware.asyncexitstack import AsyncExitStackMiddleware
from fastapi.middleware.cors import CORSMiddleware


from . import (config, exceptions, extensions, middlewares, routers, security,
               v100)
from .extensions import app
from .routers import dev, latest

# ---------------
# | API ROUTERS |
# ---------------

app.include_router(dev)
app.include_router(latest)
app.include_router(v100.app)