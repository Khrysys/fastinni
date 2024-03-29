from create_certs import cert_gen
from create_secrets import gen_secrets
from create_admin import create_admin

def gen_env_file(*, file:str='.env'):
    f = open(file, 'w')
    f.write(f'EXTERNAL_HOST=127.0.0.1\nEXTERNAL_PORT=8000\nDB_URL=postgresql+psycopg://postgres:postgres@127.0.0.1:5432/db-fastinni\n\nGOOGLE_CLIENT_ID=REPLACE_THIS\nGOOGLE_CLIENT_SECRET=REPLACE_THIS\n\n')
    f.close()

    cert_gen(ENV_FILE=file)
    secrets = gen_secrets(file)
    create_admin(secrets['LOGIN_SECRET'], file)


if __name__ == '__main__':
    gen_env_file()