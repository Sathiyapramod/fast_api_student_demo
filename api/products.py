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
def get_product_by_id(id: int, dbs: Session = Depends(connect_db)):
    data = dbs.query(Products).filter(Products.id == id).first()
    return {"message": f"gets all product by id - {id}"}


@products.post("/")
def create_product(new_item: ProductSchema, dbs: Session = Depends(connect_db)):

    current_item = Products(
        product_name=new_item.product_name, description=new_item.description
    )
    dbs.add(current_item)
    dbs.commit()
    dbs.refresh(current_item)
    return {"message": "product created"}


@products.put("/{id}")
def update_product(id: int, new_item: ProductSchema):
    valid_entry = dbs.query(Products).filter(Products.id == id).first()
    if not data:
        return {"message": "no data available"}
    else:
        valid_entry.product_name = new_item.product_name
        valid_entry.description = new_item.description
        dbs.commit()
        dbs.refresh(valid_entry)
        return {"message": "updates product by id"}


@products.delete("/{id}")
def delete_product(id: int):
    valid_entry = dbs.query(Products).filter(Products.id == id).first()
    if not data:
        return {"message": "no data available"}
    else:
        dbs.delete(valid_entry)
        dbs.commit()
        dbs.refresh()
        return {"message": "Deleted successfullys"}
