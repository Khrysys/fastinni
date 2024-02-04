from os import path
from create_certs import cert_gen
from create_secrets import gen_csrf_secret, gen_login_secret

def gen_env_file(*, file='.env'):
    cert_gen(ENV_FILE=file)
    gen_csrf_secret(file)
    gen_login_secret(file)

    if path.exists(".env"):
        f = open(file, 'a')
    else:
        f = open(file, 'w')
    f.write(f'\HOST=127.0.0.1\nPORT=8000\nDB_URL=postgresql+psycopg://postgres:postgres@127.0.0.1:5432/db-fastinni')
    f.close()

if __name__ == '__main__':
    gen_env_file()