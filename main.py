from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal, Base, engine
from schema import StudentMarks, UpdateStudentData
from models import Marks

app = FastAPI()

# orm to synchronize with database
Base.metadata.create_all(bind=engine)

def connect_db():
    db = SessionLocal()
    try:
        print("Db connected successfully")
        yield db
    finally:
        db.close()


@app.get("/test")
def welcome_kit():
    print("hello world")
    return {"message": "Welcome to our server"}


# get all marks
@app.get("/marks", status_code=status.HTTP_200_OK)
def get_all_marks(db: Session = Depends(connect_db)):
    # raw_query = "SELECT * FROM marks;"
    # items = db.execute(text(raw_query)).fetchall()
    items = db.query(Marks).all()
    return items


# get marks by id
@app.get("/marks/{student_id}")
def get_marks_by_id(
    student_id: int, student_name: str, db: Session = Depends(connect_db)
):
    current_item = db.query(Marks).filter(Marks.student_id == student_id).first()
    return current_item


# step 2
# create a class for the student marks
# create marks
@app.post("/marks")
def create_marks(new_marks: StudentMarks, dbs: Session = Depends(connect_db)):
    # extract separate data
    my_name = new_marks.student_name
    ps_mark = new_marks.ps
    tech_mark = new_marks.tech
    english = new_marks.english
    ls = new_marks.lifeskills

    new_entry = Marks(
        student_name=my_name, ps=ps_mark, tech=tech_mark, english=english, lifeskills=ls
    )
    # adding the new entry
    dbs.add(new_entry)

    # committing the transaction
    dbs.commit()

    # refresh the object
    dbs.refresh(new_entry)
    return new_entry


# student_id is called Request Params
# revised_marks is called Request Body (or) Payload
@app.put("/marks/{student_id}")
def update_marks(
    student_id: str, revised_marks: UpdateStudentData, db: Session = Depends(connect_db)
):
    db_mark = db.query(Marks).filter(Marks.student_id == student_id).first()
    if not db_mark:
        return {"message": f"Invalid Student id - {student_id}"}
    else:
        db_mark.english = revised_marks.english
        db_mark.lifeskills = revised_marks.lifeskills
        db_mark.ps = revised_marks.ps
        db_mark.tech = revised_marks.tech

        db.commit()

        db.refresh(db_mark)
        return {"message": "Mark updated successfully"}


@app.delete("/marks/{student_id}")
def delete_marks(student_id: str, db: Session = Depends(connect_db)):
    # write your code logic here
    db_mark = db.query(Marks).filter(Marks.student_id == student_id).first()
    if not db_mark:
        return {"message": f"Invalid Student id - {student_id}"}
    else:
        db.delete(db_mark)
        db.commit()
        return {"message": "marks deleted successfully"}
