from pydantic import BaseModel


class InvoiceSchema(BaseModel):
    id: int
    invoice_no: str
    c_name: str
