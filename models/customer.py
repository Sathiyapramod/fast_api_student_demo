from sqlalchemy import Column, Integer, String
from db.database import Base

class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    email = Column(String)
    