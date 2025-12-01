from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from dependencies import connect_db
from models.customer import Customers
from schemas.customer import Customers as CustomerSchema

router = APIRouter(prefix="/customers")

@router.get("/")
def get_all_customers(dbs: Session = Depends(connect_db)):
    customer_list = dbs.query(Customers).all()
    print(customer_list)
    return {"message": "all customers"}


@router.get("/{id}")
def get_customer_by_id(id: int):
    return {"message": f"customer by {id}"}


@router.post("/")
def create_customer(new_customer_entry: CustomerSchema):
    return {"message": "create a customer"}


@router.put("/{id}")
def update_customer(id: int):
    return {"message": "update a customer"}


@router.delete("/{id}")
def delete_customer(id: int):
    return {"message": "delete a customer"}
