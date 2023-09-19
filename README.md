# Fastinni

This app is intended to be a FastAPI / React Single-Page web app starting point, inspired by my conversations with the developer of [Flaskinni](https://github.com/dadiletta/flaskinni). It builds itself wholy through the command line, has builtin admin roles and table web views, all in a beautiful React frontend. 

## Requirements

- npm
- python3.11
- poetry
- A handy .env file

That's it! simply install the poetry dependencies and Fastinni takes care of the rest, the babel translation, webpack, tying things up into a single neat directory. 

## Running the App

### Windows

```sh
git clone https://github.com/Khrysys/fastinni
cd fastinni
pip install --upgrade poetry
python -m poetry shell
poetry install
poetry run main.py
```

### MacOS / Linux

```sh
git clone https://github.com/Khrysys/fastinni
cd fastinni
pip3 install --upgrade poetry
python3 -m poetry shell
poetry install
poetry run main.py
```

## Sample `.env` File

```env
# -----------------------
# | NODE.JS ENVIRONMENT |
# -----------------------
NPM_API_URL=https://127.0.0.1:5000/api/latest/
# Used to provide easy splitting up of the API server and the HTML server

# --------------------------------
# | FASTINNI HOSTING ENVIRONMENT |
# --------------------------------
FASTINNI_HOST=127.0.0.1
FASTINNI_PORT=5000
FASTINNI_DB_URL=postgresql+asyncpg://postgres:postgres@localhost/db-fastinni 
# FASTINNI_UNIX_SOCKET=/run/ #
FASTINNI_SSL_KEYFILE=private.key
FASTINNI_SSL_CERTFILE=selfsigned.crt
```
