from create_certs import cert_gen
from create_secrets import gen_csrf_secret

def gen_env_file(*, file='.env'):
    cert_gen(ENV_FILE=file)
    gen_csrf_secret(file)