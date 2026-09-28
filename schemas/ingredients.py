from pydantic import BaseModel


class IngredientSchema(BaseModel):
    ingredient_name: str
    quantity: str
