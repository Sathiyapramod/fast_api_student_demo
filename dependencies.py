from db.database import SessionLocal


def connect_db():
    # start
    # connection operation
    db = SessionLocal()
    try:
        print("Connected to DB successfully")
        yield db
    except:
        db.close()
    # stop
