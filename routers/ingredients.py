from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependencies import connect_db
from models.ingredients import Ingredients
from schemas.ingredients import IngredientSchema

ingredients_router = APIRouter(prefix="/ingredients", tags=["Ingredients"])


@ingredients_router.get("/", status_code=status.HTTP_200_OK)
def get_all_ingredients(dbs: Session = Depends(connect_db)):
    ingredients = dbs.query(Ingredients).all()
    return ingredients


@ingredients_router.post("/", status_code=status.HTTP_200_OK)
def create_ingredient(new_ingred: IngredientSchema, dbs: Session = Depends(connect_db)):
    new_entry = Ingredients(
        ingredient_name=new_ingred.ingredient_name,
        quantity=new_ingred.quantity
    )

    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)
