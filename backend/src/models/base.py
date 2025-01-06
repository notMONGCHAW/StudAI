from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase

Model1Base = declarative_base()

class testObj(Model1Base):
    __tablename__ = "testObj"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    cmt = Column(String)
