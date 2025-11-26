from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

username = "postgres"
password = "root"
hostname = "localhost"
port = "5432"
db_name = "wednesday"

DB_URL = f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db_name}"

# dialling operation
engine = create_engine(DB_URL)

# binding the engine to a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# this needs to be imported inside models.py
Base = declarative_base()
