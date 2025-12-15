from sqlalchemy import Column, String, Integer
from db.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, index=True)
    username = Column(String)
    password = Column(String)
