from sqlalchemy import Column, Integer, String
from ..database.session import Session 
from .session import Base
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)