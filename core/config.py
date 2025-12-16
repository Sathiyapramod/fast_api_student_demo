from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
hostname = os.getenv("DB_HOSTNAME")
port = os.getenv("DB_PORT")
db_name = os.getenv("DATABASE")

# JWT configurations
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 30
