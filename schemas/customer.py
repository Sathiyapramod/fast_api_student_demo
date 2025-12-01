from pydantic import BaseModel


class Customers(BaseModel):
    customer_name: str
    email: str
