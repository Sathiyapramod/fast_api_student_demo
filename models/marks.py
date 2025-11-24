from sqlalchemy import Column, Integer, String
from database import Base


class Marks(Base):
    __tablename__ = "marks"

    student_id = Column(Integer, index=True, primary_key=True)
    student_name = Column(String)
    ps = Column(Integer)
    tech = Column(Integer)
    english = Column(Integer)
    lifeskills = Column(Integer)


