from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...database.session import SessionLocal  # Adjusted import
from ...services.course_service import create_course, get_courses  # Adjusted import

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/courses/")
def add_course(title: str, description: str, db: Session = Depends(get_db)):
    return create_course(db=db, title=title, description=description)

@router.get("/courses/")
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_courses(db=db, skip=skip, limit=limit)