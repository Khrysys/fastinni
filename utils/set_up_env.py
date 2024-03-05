from typing import Any


def input_with_default(message: str, default: Any):
    var = input(f'{message} ({default}): ')
    if var == '':
        var = default
        
    return var

def ask_choice(message: str, default: bool) -> bool:
    d = 'yes' if default is True else 'no'
    var = input_with_default(f'{message}', f'yes/no -> {d}')
    
    if var == 'yes':
        return True
    return False
    
    

def main():
    fname = input_with_default('Enter the name of the ENV file', '.env')
    f = open(fname, 'w')
        
    host = input_with_default('Enter the external host (without port) that the API should listen to', '127.0.0.1')    
    f.write(f'EXTERNAL_HOST={host}\n')
    
    port = input_with_default('Enter the port that the API should listen to', '8000')
    try:
        port = int(port)
    except:
        print('Port must be an int!')
        exit(1)
    f.write(f'EXTERNAL_PORT={port}\n')
    
    choice = ask_choice('Customize the database URL (default postgres+asyncpg://postgres:postgres@127.0.0.1:5432/db-fastinni)', False)
    
    if choice is False:
        username = input_with_default('Database username', 'postgres')
        password = input_with_default('Database password', 'postgres')
        db_host = input_with_default('Database host', '127.0.0.1')
        db_port = input_with_default('Database port', '5432')
        name = input_with_default('Database name', 'db-fastinni')
        db_url = f'postgres+asyncpg://{username}:{password}@{db_host}:{db_port}/{name}'
    else:
        db_url = 'postgres+asyncpg://postgres:postgres@127.0.0.1:5432/db-fastinni'
    f.write(f'DB_URL={db_url}\n\n')
    
    google_client_id = input_with_default('Copy your OAuth Google Client ID' , 'REPLACE')
    f.write(f'GOOGLE_CLIENT_ID={google_client_id}\n')
    google_client_secret = input_with_default('Copy your OAuth Google Client Secret', 'REPLACE')
    f.write(f'GOOGLE_CLIENT_ID={google_client_secret}\n\n')
    
    choice = ask_choice('Generate Self Signed SSL certificates?', False)
    
    if choice is True:
        import create_certs
        key_file = input_with_default('Name of Key File', 'private.key')
        cert_file = input_with_default('Name of Cert File', 'selfsigned.crt')
        create_certs.cert_gen(key_file, cert_file, fname)
    else:
        choice = ask_choice('Add SSL Certificates from elsewhere?', True)
        
        if choice is True:
            key_file = input_with_default('Relative path to key file', 'private.key')
            cert_file = input_with_default('Relative path to cert file', 'selfsigned.crt')
            f.write(f'SSL_KEYFILE={key_file}\nSSL_CERTFILE={cert_file}\n\n') # type: ignore
            
            
    
    choice = ask_choice('Generate Randomized Secrets?', True)
    
    if choice:
        import create_secrets
        create_secrets.gen_secrets(f)
    else:
        f.write('CSRF_SECRET=secret')
        f.write('LOGIN_SECRET=secret')
    
    choice = ask_choice('Add Admin account?', True)
    
    f.close()
    

if __name__ == '__main__':
    main()