from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# create a class for the student marks
class StudentMarks(BaseModel):
    student_id: str
    ps: int
    tech: int
    english: int
    lifeskills: int


@app.get("/test")
def welcome_kit():
    print("hello world")
    return {"message": "Welcome to our server"}


# get all marks
@app.get("/marks")
def get_all_marks():
    return {"message": "This end point will return all the marks"}


# get marks by id
@app.get("/marks/{student_id}")
def get_marks_by_id(student_id: int):
    print(student_id)
    return {
        "message": f"This end point will return marks for student no - {student_id}"
    }


# create marks
@app.post("/marks")
def create_marks(new_marks: StudentMarks):
    print(new_marks)
    pass
