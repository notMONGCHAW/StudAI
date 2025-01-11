from fastapi import FastAPI
from api.endpoints.courses import router as courses_router


# Initialize FastAPI app
app = FastAPI(
    title="Courses API",
    description="A simple API to manage courses.",
    version="1.0.0",
)

# Root endpoint
@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint to provide a welcome message.
    """
    return {"message": "Welcome to the Courses API!"}

# Include the courses router
app.include_router(courses_router, prefix="/courses", tags=["Courses"])

# Run the application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
