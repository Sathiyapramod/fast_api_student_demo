from fastapi import APIRouter, status, Depends
from models.products import Products
from schemas.products import ProductSchema
from sqlalchemy.orm import Session
from dependencies import connect_db

products_router = APIRouter(prefix="/products", tags=["Products"])

@products_router.get("/", status_code=status.HTTP_200_OK)
def get_all_products(dbs: Session = Depends(connect_db)):
    products = dbs.query(Products).all()
    return products


@products_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_product_by_id(id: int, dbs: Session = Depends(connect_db)):
    valid_product = dbs.query(Products).filter(Products.id == id).first()
    if not valid_product:
        return {"message": f"product id {id} is invalid"}
    return valid_product


@products_router.post("/", status_code=status.HTTP_200_OK)
def create_product(new_product: ProductSchema, dbs: Session = Depends(connect_db)):
    valid_entry = Products(
        product_name=new_product.product_name, ingredient_id=new_product.ingredient_id
    )

    dbs.add(valid_entry)
    dbs.commit()
    dbs.refresh(valid_entry)
    return {"message": "created new product"}

