# File path: e:/project show/studai/backend/src/services/course_service.py

from sqlalchemy.orm import Session

from ..models.base import testObj


# Adjust the import based on your structure

def create_course(db: Session, title: str, description: str):
    db_course = testObj(title=title, description=description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(testObj).offset(skip).limit(limit).all()