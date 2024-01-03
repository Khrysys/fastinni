from create_certs import cert_gen
from create_secrets import gen_csrf_secret, gen_login_secret

def gen_env_file(*, file='.env'):
    cert_gen(ENV_FILE=file)
    gen_csrf_secret(file)
    gen_login_secret(file)

if __name__ == '__main__':
    gen_env_file()