BITLENGTH = 256

from secrets import randbits

def gen_secrets(file:str='.env') -> dict[str, str]:
    with open(file, 'a') as f:
        secret = randbits(BITLENGTH).to_bytes(int(BITLENGTH / 8)).hex()
        ret = {'CSRF_SECRET': secret}
        f.write(f'CSRF_SECRET={secret}\n')
        secret = randbits(BITLENGTH).to_bytes(int(BITLENGTH / 8)).hex()
        ret['LOGIN_SECRET'] = secret
        f.write(f'LOGIN_SECRET={secret}\n\n')
        return ret

if __name__ == '__main__':
    print('This script should not be run in standalone mode! run one of the generator files instead.')