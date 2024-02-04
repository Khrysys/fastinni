BITLENGTH = 256

from secrets import randbits
from os import path

def gen_csrf_secret(file='.env'):
    secret = randbits(BITLENGTH)
    if path.exists(".env"):
        f = open(file, 'a')
    else:
        f = open(file, 'w')
    f.write(f'CSRF_SECRET={secret.to_bytes(int(BITLENGTH / 8)).hex()}\n')
    f.close()
        
def gen_login_secret(file='.env'):
    secret = randbits(BITLENGTH)
    if path.exists(file):
        f = open(file, 'a')
    else:
        f = open(file, 'w')
    f.write(f'LOGIN_SECRET={secret.to_bytes(int(BITLENGTH / 8)).hex()}\n')
    f.close()

def gen_secrets(file='.env'):
    gen_csrf_secret(file)
    gen_login_secret(file)

if __name__ == '__main__':
    gen_secrets()