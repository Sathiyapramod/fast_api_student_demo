import jwt
from core.config import ALGORITHM, SECRET_KEY


def create_access_token(data: dict):
    data_to_encode = data.copy()
    data_to_encode.update({"exp": 86400})
    encoded_token = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_token
