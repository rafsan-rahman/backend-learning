from sqlalchemy import Column, Integer, VARCHAR, BIGINT, Text
from config import Base

class Employee(Base):
    __tablename__ = "employee"
    
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    salary = Column(BIGINT)