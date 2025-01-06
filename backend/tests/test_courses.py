from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from ..src.models.base import testObj


def test_create_course(client: TestClient , db: Session):
    # Test creating a course
    course_data = {
        "title": "Test Course",
        "description": "A test course description",
        "cmt": "haka hu nana"
    }
    
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 200
    
    # Verify the course was created in the database
    created_course = response.json()
    assert created_course['title'] == course_data['title']
    assert created_course['description'] == course_data['description']
    assert created_course['cmt'] == course_data['cmt']

def test_get_courses(client: TestClient, db: Session):
    # Ensure there are courses in the database
    test_course = testObj(
        title="Sample Course", 
        description="Sample Description",
        cmt="haka hu nana"
    )
    db.add(test_course)
    db.commit()
    
    # Test retrieving courses
    response = client.get("/courses/")
    assert response.status_code == 200
    
    courses = response.json()
    assert len(courses) > 0
    
    # Verify course details
    assert any(course['title'] == "Sample Course" for course in courses)
    assert any(course['cmt'] == "haka hu nana" for course in courses)

def test_create_course_validation(client: TestClient):
    # Test creating a course with invalid data
    invalid_course_data = {
        "title": "",  # Empty title
        "description": None,  # Invalid description
        "cmt": ""  # Optional: test cmt field validation
    }
    
    response = client.post("/courses/", json=invalid_course_data)
    assert response.status_code == 422  # Unprocessable Entity