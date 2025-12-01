from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal, engine, Base
from api.invoices import invoices as invoiceRouter
from api.products import products as productsRouter

app = FastAPI()
app.include_router(invoiceRouter)
app.include_router(productsRouter)

Base.metadata.create_all(bind=engine)

def connect_db():
    db = SessionLocal()
    try:
        print("Connected to DB successfully")
        yield db
    finally:
        db.close()


@app.get("/test")
def welcome_kit(dbs: Session = Depends(connect_db)):
    return {"message": "Welcome to our server"}
