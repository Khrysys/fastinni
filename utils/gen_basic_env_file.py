from os import path
from create_certs import cert_gen
from create_secrets import gen_secrets

def gen_env_file(*, file='.env'):
    if path.exists(".env"):
        f = open(file, 'a')
    else:
        f = open(file, 'w')
    f.write(f'HOST=127.0.0.1\nPORT=8000\nDB_URL=postgresql+psycopg://postgres:postgres@127.0.0.1:5432/db-fastinni\n\nGOOGLE_CLIENT_ID=REPLACE_THIS\nGOOGLE_CLIENT_SECRET=REPLACE_THIS\n\n')
    f.close()

    cert_gen(ENV_FILE=file)
    gen_secrets(file)


if __name__ == '__main__':
    gen_env_file()