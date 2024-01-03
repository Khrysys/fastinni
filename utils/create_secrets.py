BITLENGTH = 256

from secrets import randbits
from os import path

def gen_csrf_secret(file='.env'):
    secret = randbits(BITLENGTH)
    if path.exists(".env"):
        f = open(file, 'a')
    else:
        f = open(file, 'w')
    f.write(f'\nCSRF_SECRET={secret.to_bytes(int(BITLENGTH / 8)).hex()}')
    f.close()
        
def gen_login_secret(file='.env'):
    secret = randbits(BITLENGTH)
    if path.exists(".env"):
        f = open(file, 'a')
    else:
        f = open(file, 'w')
    f.write(f'\nLOGIN_SECRET={secret.to_bytes(int(BITLENGTH / 8)).hex()}')
    f.close()

if __name__ == '__main__':
    gen_csrf_secret()