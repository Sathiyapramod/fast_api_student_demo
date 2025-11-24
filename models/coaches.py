from sqlalchemy import Column, Integer, String
from database import Base

class Coaches(Base):

    __tablename__ = "coaches"

    coach_id = Column(Integer, index=True, primary_key=True)
    coach_name = Column(String)
