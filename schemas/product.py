from pydantic import BaseModel

class ProductSchema(BaseModel):
    product_name: str
    description: str
