from db.database import SessionLocal, engine, Base

def connect_db():
    db = SessionLocal()
    try:
        print("Connected to DB successfully")
        yield db
    finally:
        db.close()
