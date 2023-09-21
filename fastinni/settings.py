'''
    Loads the settings from environment and performs checks to ensure the values are valid
'''
from os import getenv, urandom

'''SQL Database URL (default: postgresql+asyncpg://postgres:postgres@localhost/db-fastinni)'''
FASTINNI_DB_URL = getenv("FASTINNI_DB_URL", "postgresql://postgres:postgres@localhost/db-fastinni")

FASTINNI_SESSION_SECRET_KEY = getenv('FASTINNI_SESSION_SECRET_KEY', urandom(128).hex())

FASTINNI_CSRF_TOKEN = getenv('FASTAPI_CSRF_TOKEN', str(urandom(128).hex()))
FASTINNI_CSRF_COOKIE_SAMESITE = getenv('FASTINNI_CSRF_COOKIE_SAMESITE', 'none')
FASTINNI_CSRF_COOKIE_SECURE = getenv('FASTINNI_CSRF_COOKIE_SECURE', True)
FASTINNI_CSRF_COOKIE_HTTPONLY = getenv('FASTINNI_CSRF_COOKIE_HTTPONLY', False)

FASTINNI_MAIL_USERNAME = getenv("FASTINNI_MAIL_USERNAME", "Fastinni")
FASTINNI_MAIL_PASSWORD = getenv("FASTINNI_MAIL_PASSSWORD", "password")
FASTINNI_MAIL_PORT = getenv("FASTINNI_MAIL_PORT", 465)
FASTINNI_MAIL_SERVER = getenv("FASTINNI_MAIL_SERVER", "smtp.gmail.com")
FASTINNI_MAIL_STARTTLS = getenv("FASTINNI_MAIL_STARTTLS", False)
FASTINNI_MAIL_SSL_TLS = getenv("FASTINNI_MAIL_SSL_TLS", True)
FASTINNI_MAIL_DEBUG = getenv("FASTINNI_MAIL_DEBUG", 0)
FASTINNI_MAIL_FROM = getenv("FASTINNI_MAIL_FROM", "fastinni@gmail.com")
