from sqlalchemy import Column, String, Integer
from database import Base


# base is your parent class
class Marks(Base):
    # defining the table name
    __tablename__ = "marks"

    student_id = Column(Integer, primary_key=True)
    student_name = Column(String)
    ps = Column(Integer)
    english = Column(Integer)
    tech = Column(Integer)
    lifeskills = Column(Integer)


# create one class called coaches
class Coaches(Base):
    # defining table name
    __tablename__ = "coaches"

    # column names
    coach_id = Column(Integer, primary_key=True)
    coach_name = Column(String)
    email = Column(String)
