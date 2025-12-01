from fastapi import APIRouter

invoices = APIRouter(prefix="/invoices", tags=["invoices"])

@invoices.get("/")
def get_invoices():
    return {"message": "gets all invoices"}


@invoices.get("/{id}")
def get_invoice_by_id(id: int):
    return {"message": f"gets an invoice by id - {id}"}


@invoices.post("/")
def create_invoice():
    return {"message": "creates a invoice"}


@invoices.put("/{id}")
def update_invoice(id: int):
    return {"message": f"updates invoice by id - {id}"}
