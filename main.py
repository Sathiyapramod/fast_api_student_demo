from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal, engine
from models import Base, Marks, Coaches
from schema import StudentsData

app = FastAPI()

Base.metadata.create_all(bind=engine)

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


@app.get("/test")
def welcome_kit(dbs: Session = Depends(connect_db)):
    return {"message": "Welcome to our server"}


# get all marks
@app.get("/marks")
def get_all_marks(dbs: Session = Depends(connect_db)):
    # how to query
    # raw_query = "SELECT * FROM marks"
    # list_of_marks = dbs.execute(text(raw_query)).fetchall()

    list_of_marks = dbs.query(Marks).all()
    print(list_of_marks)
    return list_of_marks


# get marks by id
@app.get("/marks/{student_id}")
def get_marks_by_id(student_id: str, dbs: Session = Depends(connect_db)):

    valid_entry = dbs.query(Marks).filter(Marks.student_id == student_id).first()
    print(valid_entry)

    if not valid_entry:
        return {"message": "invalid id"}
    else:
        return valid_entry
# create marks
@app.post("/marks")
def create_marks(new_marks: StudentsData, dbs: Session = Depends(connect_db)):
    # extract separate data
    my_name = new_marks.student_name
    ps_mark = new_marks.ps
    tech_mark = new_marks.tech
    english = new_marks.english
    ls = new_marks.lifeskills

    new_entry = Marks(
        student_name=my_name,
        ps=ps_mark,
        tech=tech_mark,
        english=english,
        lifeskills=ls,
    )

    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)
    return new_entry


# student_id is called Request Params
# revised_marks is called Request Body (or) Payload
@app.put("/marks/{student_id}")
def update_marks(
    student_id: str,
    revised_marks: StudentsData,
    dbs: Session = Depends(connect_db),
):
    # check whether the given id is matching or not
    valid_entry = dbs.query(Marks).filter(Marks.student_id == student_id).first()
    if not valid_entry:
        return {"message": "Id is invalid"}
    else:
        english = revised_marks.english
        ps = revised_marks.ps
        tech = revised_marks.tech
        ls = revised_marks.lifeskills
        name = revised_marks.student_name

        # updation
        # name
        valid_entry.student_name = name
        # marks
        valid_entry.ps = ps
        valid_entry.tech = tech
        valid_entry.lifeskills = ls
        valid_entry.english = english

        # commit
        dbs.commit()

        dbs.refresh(valid_entry)
        return {"message": "Updated successfully"}


@app.delete("/marks/{student_id}")
def delete_marks(student_id: str):
    # write your code logic here
    pass
