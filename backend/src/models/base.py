from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

Base = DeclarativeBase()

class testObj(Base):
    __tablename__ = "testObj"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)