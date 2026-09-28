from pydantic import BaseModel


class ProductSchema(BaseModel):
    product_name: str
    ingredient_id: int
