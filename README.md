# Fastinni

Fastinni is a project inspired by conversations with the developer of [Flaskinni](https://github.com/dadiletta/flaskinni). It serves as a starter FastAPI application with the following stack:

1. **[SQLModel Database](https://sqlmodel.tiangolo.com/)**: Tested with PostgresQL, it stores users, OAuth2 client registrations, roles, groups, blog posts, and more.

2. **[FastAPI & Python](https://fastapi.tiangolo.com/)**: FastAPI simplifies managing a stateless server. Additional libraries like FastAPI-CSRF-Protect and FastAPI-Mail enhance functionality.

3. **[Uvicorn](https://www.uvicorn.org/)**: Uvicorn serves as the ASGI framework, replacing WSGI frameworks like Gunicorn.

4. **[ReactJS Frontend](https://react.dev/)**: Provides an appealing display for the application's complex functionality.

In addition to these main components, other elements such as a reverse proxy (e.g., NGINX or Apache) for added robustness and cloud products like AWS, Cloudflare, or Google Cloud to mitigate DDOS and other attacks may be incorporated. However, for the most part, these components suffice to initiate a FastAPI/React full stack project.

## Installation Guide

Clone down the repository and move into the directory

```sh
git clone https://github.com/khrysys/fastinni
cd fastinni
```

In order to install Fastinni properly on your machine, you must have Python 3.10 or later, NPM 9, and PostgresQL 15 already installed on your machine. NPM versions may or may not work, but this project is tested on Python 3.11 and NPM 9.6.7. 

After installing those, install Poetry:

```sh
pip install poetry
```

Now that poetry is installed, open the virtual environment's shell and install the dependencies.

```sh
poetry shell
poetry install
```

***NOTE: PyOpenSSL can be installed as the dev dependency group. This is required to test OAuth locally by creating self-signed SSL certificates, and is not a requirement for production, since in production you are expected to provide properly signed certs. It can certainly be installed, but why?***

```sh
# Installing the dev dependency group
poetry install --with=dev
```


## Setting up the .env file

For development, there is a `utils/gen_env_file.py` that automatically creates secure secrets for development. ***This does require the dev dependency group.***

Run the script.

```sh
python utils/gen_env_file.py
```

This will set up a basic .env file for you. Note that the default values are as shown: 

```env

SSL_KEYFILE=private.key
SSL_CERTFILE=selfsigned.crt
CSRF_SECRET=837ece9526a590792248b2d5cdd2ffb4382eac29539bec12a609cfe559a3e9af
LOGIN_SECRET=2dc2adab8102922bccba09d0da0dbc913655b3b76bc83109f2aeeca3ccf608a3\HOST=127.0.0.1
PORT=8000
DB_URL=postgresql+psycopg://postgres:postgres@127.0.0.1:5432/db-fastinni
```

## Transpiling The React scripts

Fastinni is not just the API, it also has a React frontend. This is where NPM comes in. Install the dependencies with the following command:

```sh
npm install
```

From here, there are three compilation scripts, `pack`, `produce`, and `produce-win`. The one we'll be using is `pack`

```sh
npm run pack
```

You should now see a directory called `html` that contains the transpiled React code.

## Running the app

Now that the API dependencies are running, verify you can run the app with the following command:

```sh
python -m api
```

You should see FastAPI initialize to `http://127.0.0.1:8000`. But you'll discover that signup and login through third party providers like Google are not possible. Let's fix this. 

## Setting up Third Party Login