
from secrets import randbits
from jwt import encode
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_admin(login_secret: str, env_file:str='.env'):
    with open(env_file, 'a') as f:
        token = str(encode({
            "id": 0, 
            "tag": 'Admin', 
            "password": pwd_context.hash(randbits(64).to_bytes(int(8)).hex()), 
            "google_id": None,
            "admin": True,
        }, login_secret))
        f.write(f'ADMIN_LOGIN_JWT={token}')