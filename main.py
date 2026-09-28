import random

import gradio as gr
from fastapi import Depends, FastAPI, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from db.database import Base, SessionLocal, engine
from routers.marks import marks_router
from routers.products import products_router
from routers.users import users_router

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/test", status_code=status.HTTP_200_OK)
def welcome_kit():
    return {"message": "Welcome to our server"}


# app.include_router(users_router)
# app.include_router(marks_router)
# app.include_router(products_router)


def random_response():
    return random.choice(["Hello!", "How are you?", "What's up?", "Nice to meet you!"])


gr.ChatInterface(
    fn=random_response
).launch()
