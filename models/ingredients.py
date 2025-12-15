from sqlalchemy import Column, String, Integer
from db.database import Base


class Ingredients(base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    ingredient_name = Column(String)
    quantity = Column(Integer)