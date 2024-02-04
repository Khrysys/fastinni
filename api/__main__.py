# Main file
# This creates the core app, adds the API and StaticFiles, and runs itself via uvicorn.
# This does not create an NGinx instance or check the NGinx config, that should be done seperately.

# run with `python -m api`



from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn import Server, Config
from os import getenv
from asyncio import run

load_dotenv()

# Rename the app in this file, since it's declared as app in __init__.py
from . import app as api

app = FastAPI(title="Fastinni", docs_url=None, redoc_url=None)
app.mount('/api', api)
app.mount('/', StaticFiles(directory='html', html=True))



# FastAPI is responsible for all of the actual code, but uvicorn is what makes it web compatible.
uvicorn_config = Config(
    app                       = app,
    host                      = getenv("HOST", "127.0.0.1"),
    port                      = int(getenv("PORT", 8000)),
    reload                    = bool(getenv("RELOAD", True)),
    ssl_certfile              = getenv("SSL_CERTFILE"), # type: ignore
    ssl_keyfile               = getenv("SSL_KEYFILE"), # type: ignore
    timeout_graceful_shutdown = 1
)

# Server object. This is the main Uvicorn object, and there's lots of fancy things that can be expanded from here.
uvicorn_server = Server(uvicorn_config)

# --- ONLY HAVE ONE OF THESE OPTIONS OTHERWISE THINGS WILL PROBABLY BREAK. maybe. idk
# Run linearly
#uvicorn_server.run()
# Run asynchronously
run(uvicorn_server.serve())