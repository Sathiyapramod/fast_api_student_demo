from fastapi import FastAPI
from routers.customers import router as customer_router
from db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(customer_router)


@app.get("/")
def welcome_route():
    return {"message": "welcome to server"}
