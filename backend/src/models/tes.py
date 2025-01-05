from sqlalchemy import Column, Integer, String

from ..database.session import Base

class aaa(Base):
    __tablename__ = "ABSC"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)