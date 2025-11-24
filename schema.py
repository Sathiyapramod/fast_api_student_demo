from pydantic import BaseModel

class StudentMarks(BaseModel):
    student_id: str
    student_name: str
    ps: int
    tech: int
    english: int
    lifeskills: int


class UpdateStudentData(BaseModel):
    student_name: str
    ps: int
    tech: int
    english: int
    lifeskills: int
