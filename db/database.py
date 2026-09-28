from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from core.config import db_name, hostname, password, port, username

DB_URL = f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db_name}"

# dialling operation
engine = create_engine(DB_URL)

# binding the engine to a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# this needs to be imported inside models.py
Base = declarative_base()
