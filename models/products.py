from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Products(base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    # foreign keys
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    # relationships
    ingred_products = relationship("ingredients")
