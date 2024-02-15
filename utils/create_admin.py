def create_admin(emailAddress="admin@fastinni.dev", password='fastinni', display_name="Super Administrator", ENV_FILE='.env'):
    with open(ENV_FILE, 'a') as f:
        f.write(f'ADMIN_EMAIL={emailAddress}\n')
        f.write(f'ADMIN_PASSWORD={password}\n')
        f.write(f'ADMIN_DISPLAY_NAME={display_name}\n\n')