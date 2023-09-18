# Fastinni

This app is intended to be a FastAPI / React Single-Page web app starting point, inspired by my conversations with the developer of [Flaskinni](https://github.com/dadiletta/flaskinni). It builds itself wholy through the command line, has builtin admin roles and table web views, all in a beautiful React frontend. 

## Requirements

- npm
- python3.11
- poetry

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
