from dotenv import load_dotenv
load_dotenv()

from api import app as api

if __name__ == '__main__':
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles
    from os import getenv
    
    app = FastAPI(docs_url=None, redoc_url=None)
    app.mount("/api", api)
    app.mount("/", StaticFiles(directory="html", html=True))

    from uvicorn import Server, Config
    config = Config(
        app = app,
        host = getenv("HOST", "127.0.0.1"),
        port = int(getenv("PORT", 8000)),
        reload=bool(getenv("RELOAD", True)),
        ssl_certfile=getenv("SSL_CERTFILE"),
        ssl_keyfile=getenv("SSL_KEYFILE")
    )

    server = Server(config)

    from asyncio import run
    run(server.serve())