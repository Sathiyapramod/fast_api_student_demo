from sqlalchemy import Column, String, Integer
from database import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, index=True, primary_key=True)
    product_name = Column(String)
    description = Column(String)
