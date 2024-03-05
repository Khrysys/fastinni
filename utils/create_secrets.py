BITLENGTH = 256

from io import TextIOWrapper
from secrets import randbits

def gen_secrets(file:TextIOWrapper) -> dict[str, str]:
    secret = randbits(BITLENGTH).to_bytes(int(BITLENGTH / 8)).hex()
    ret = {'CSRF_SECRET': secret}
    file.write(f'CSRF_SECRET={secret}\n')
    secret = randbits(BITLENGTH).to_bytes(int(BITLENGTH / 8)).hex()
    ret['LOGIN_SECRET'] = secret
    file.write(f'LOGIN_SECRET={secret}\n\n')
    return ret

if __name__ == '__main__':
    print('This script should not be run in standalone mode! Run one of the generator files instead.')