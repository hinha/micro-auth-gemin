import os 
from gino.ext.sanic import Gino

def to_bool(value):
    return str(value).strip().lower() in ['1', 'true', 'yes']

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


APP_HOST = os.environ.get('APP_HOST', "127.0.0.1")
APP_PORT = to_int(os.environ.get('APP_HOST', "8000"))
APP_DEBUG = to_bool(os.environ.get('APP_DEBUG', True))
APP_WORKERS = int((os.environ.get('APP_WORKERS', 1)))
APP_SSL_CERT = os.environ.get('APP_SSL_CERT', None)
APP_SSL_KEY = os.environ.get('APP_SSL_KEY', None)
if APP_SSL_CERT and APP_SSL_KEY:
    APP_SSL = {"cert": APP_SSL_CERT, "key": APP_SSL_KEY}
else:
    APP_SSL = None


# DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
# DB_PORT = os.environ.get("DB_PORT", 5432)
# DB_NAME = os.environ.get("DB_DATABASE", "wapicklocal")
# DB_USER = os.environ.get("DB_USER", "hinhalocal")
# DB_PASSWORD = os.environ.get("DB_PASSWORD", "alongside")
DB_POOL_MIN_SIZE = to_int(os.environ.get('DB_POOL_MIN_SIZE', 5))
DB_POOL_MAX_SIZE = to_int(os.environ.get('DB_POOL_MAX_SIZE', 15))

DB_HOST = os.environ.get("DB_HOST", "services02.cg03adtwzxjo.us-east-1.rds.amazonaws.com")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_NAME = os.environ.get("DB_DATABASE", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "Qwapickdata123")


AUTHY_API_KEY = 'h9V1ScDqpeD3hj4wfX7ZPVctDCKZDg96'