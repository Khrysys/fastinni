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

In order to install Fastinni properly on your machine, you must have Python 3.10 or later, NPM 9, and PostgresQL 15 already installed on your machine.

After installing those, install Poetry:

```sh
pip install poetry
```

Now that poetry is installed, open the virtual environment's shell and install the dependencies.

```sh
poetry shell
poetry install
```

You may need to directly run it as a module depending on your PATH.

```sh
python -m poetry shell
python -m poetry install
```

***NOTE: PyOpenSSL can be installed as the dev dependency group. This is required to test OAuth locally by creating self-signed SSL certificates, and is not a requirement for production, since in production you are expected to provide properly signed certs. It can certainly be installed, but why?***

```sh
# Installing the dev dependency group
poetry install --with=dev
```


## Setting up the .env file

For development, there is a `utils/gen_env_file.py` that automatically creates secure secrets for development. ***This does require the dev dependency group to create the SSL certifications.***

Run the script.

```sh
python utils/gen_basic_env_file.py
```

This will set up a basic .env file for you. Note that the default values are as shown: 

```env
EXTERNAL_HOST=127.0.0.1
EXTERNAL_PORT=8000
DB_URL=postgresql+psycopg://postgres:postgres@127.0.0.1:5432/db-fastinni

GOOGLE_CLIENT_ID=REPLACE_THIS
GOOGLE_CLIENT_SECRET=REPLACE_THIS

SSL_KEYFILE=private.key
SSL_CERTFILE=selfsigned.crt

CSRF_SECRET=<A really long hex string>
LOGIN_SECRET=<A really long hex string>
```

You can also run `utils/set_up_env.py` and follow the steps to fully customize your enviroment.

## Transpiling The React scripts

Fastinni is not just the API, it also has a React frontend. This is where NPM is involved. Install the dependencies with the following command:

```sh
npm i
```

From here, there are three compilation scripts, `pack`, `produce`, and `produce-win`. The one we'll be using is `pack`.

```sh
npm run pack
```

You should now see a directory called `html` that contains the transpiled React code.

## Running the app

Now that the API dependencies are running, verify you can run the app with the following command:

```sh
python -m api
```

You should see Fastinni's API initialize to `https://127.0.0.1:8000`, and you can navigate to the webpage and scroll through it. But you'll discover that signup and login through third party providers like Google are not possible. Let's fix this. 

## Setting up Third Party Login

For this, you will need OAuth credentials from whichever providers you want. We'll use Google for now. Setting up those credentials is outside the scope of this article. There are many good tutorials on the internet for doing so. 

Once you have the ID and the Secret for your client, simply replace those values inside of your `.env` file.

```env
# Here
GOOGLE_CLIENT_ID=<your.client.id>
GOOGLE_CLIENT_SECRET=<your.client.secret>
```

Now when running the app and navigating to `https://127.0.0.1:8000`, you should be able to click login and then click the Google icon at the bottom of the page. If you properly copied the client ID and secret, it should allow for you to sign in. If not, follow the steps on the error message to finish setting up OAuth.

## Initializing Alembic

There is one command that needs to be run in order for Alembic to be set up. Both involve a special class that is in `api/db/__init__.py`. 

```sh
python -m api/db db-init api.db
```

Afterward, every time that you update your database, run the following.

```sh
python -m api/db db-upgrade "Commit Message"
```