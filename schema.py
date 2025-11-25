from pydantic import BaseModel


class UpdateStudentData(BaseModel):
    student_name: str
    ps: int
    tech: int
    english: int
    lifeskills: int


class StudentMarks(UpdateStudentData):
    student_id: int
