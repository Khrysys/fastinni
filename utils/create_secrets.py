BITLENGTH = 256

from secrets import randbits

def gen_secrets(file='.env'):
    with open(file, 'w') as f:
        secret = randbits(BITLENGTH)
        f.write(f'CSRF_SECRET={secret.to_bytes(int(BITLENGTH / 8)).hex()}\n')
        secret = randbits(BITLENGTH)
        f.write(f'LOGIN_SECRET={secret.to_bytes(int(BITLENGTH / 8)).hex()}\n\n')

if __name__ == '__main__':
    gen_secrets()