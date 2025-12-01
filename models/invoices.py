from sqlalchemy import Column, String, Integer
from database import Base


class Invoices(Base):
    __tablename__ = "invoices"

    id = Column(Integer, index=True, primary_key=True)
    invoice_no = Column(String)
