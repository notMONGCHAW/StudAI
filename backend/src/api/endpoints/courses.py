from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...database.session import  get_db  # Adjusted import
from ...services.course_service import create_course, get_courses  # Adjusted import

router = APIRouter()

# Dependency to get the database session


@router.post("/courses/")
def add_course(title: str, description: str, cmt:str ,db: Session = Depends(get_db)):
    return create_course(db=db, title=title, description=description,cmt=cmt)

@router.get("/courses/")
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_courses(db=db, skip=skip, limit=limit)