from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)


def connect_db():
    db = SessionLocal()
    try:
        print("Connected to DB successfully")
        yield db
    finally:
        db.close()
