from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

username = "postgres"
password = "root"
hostname = "localhost"
port = "5432"
db_name = "product_demo"

DB_URL = f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db_name}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()