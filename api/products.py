from fastapi import APIRouter, Depends
from schemas.product import ProductSchema
from dependencies import connect_db
from sqlalchemy.orm import Session
from models.products import Products

products = APIRouter(prefix="/products", tags=["products"])

@products.get("/")
def get_products(dbs: Session = Depends(connect_db)):
    data = dbs.query(Products).all()
    print(data)
    return {"message": "gets all product"}


@products.get("/{id}")
def get_product_by_id(id: int,dbs: Session = Depends(connect_db)):
    data = dbs.query(Products).filter(Products.id == id).first()
    return {"message": f"gets all product by id - {id}"}


@products.post("/")
def create_product(new_item: ProductSchema):
    return {"message": "creates a product"}


@products.put("/{id}")
def update_product(id: int, new_item: ProductSchema):
    return {"message": "updates product by id"}
