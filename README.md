# Fastinni

## Starting up

### First run

```sh
poetry shell
poetry install
python .
```

### Future runs
```sh
source $(poetry env info --path)/bin/activate
poetry install --sync
python .
```