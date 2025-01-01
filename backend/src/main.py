from fastapi import FastAPI
from .api.endpoints.courses import router as courses_router

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Courses API!"}

# Include the courses router
app.include_router(courses_router)

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)