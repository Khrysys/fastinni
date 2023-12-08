# Fastinni

This is a project designed with my conversations with the developer of [Flaskinni](https://github.com/dadiletta/flaskinni). Fastinni is intended to be a starter FastAPI application. Its stack is designed as follows:

The core application is FastAPI, with an easily production ready start by installing the production group of dependencies with any of the following commands:

```sh
# Moreso for Linux, there may be strange other things that happen if installed on other systems.
python3 -m poetry install --with=production
# Works if poetry is on PATH
poetry install --with=production
```
