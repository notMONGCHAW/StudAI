# File path: e:/project show/studai/backend/src/test_connection.py

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")

# Create the database engine
engine = create_engine(DATABASE_URL)

# Test the connection
try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print(f"Error connecting to the database: {e}")