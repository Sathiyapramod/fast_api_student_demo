from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db.database import SessionLocal, engine, Base
from routers.users import users_router
from routers.marks import marks_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/test")
def welcome_kit():
    return {"message": "Welcome to our server"}

app.include_router(users_router)
app.include_router(marks_router)