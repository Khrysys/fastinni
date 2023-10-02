npm install
npm run build
npm run pack

python -m pip install --upgrade pip
python -m pip install --upgrade poetry
python -m poetry lock
python -m poetry install --sync
uvicorn --workers 4 --host 127.0.0.1 --port 5000 --reload --reload-delay 1.5 \
    main:app