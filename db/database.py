from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

username = "postgres"
password = "root"
hostname = "localhost"
port = "5432"
db_name = "fast_api"

DB_URL = f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db_name}"

# engine creation
engine = create_engine(DB_URL)

# SessionLocal
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base
Base = declarative_base()