import os

from dotenv import load_dotenv

load_dotenv()

database_name = os.getenv("DB_TYPE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
hostname = os.getenv("DB_HOSTNAME")
port = os.getenv("DB_PORT")
db_name = os.getenv("DATABASE")

# JWT configurations
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 30
