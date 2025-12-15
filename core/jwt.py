import jwt
from config import secret_key


SECRET_KEY = secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 30


