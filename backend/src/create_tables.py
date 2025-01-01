# File path: e:/project show/studai/backend/src/create_tables.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")

# Create the database engine
engine = create_engine(DATABASE_URL)

# Import your models
from models.models import Base  # Adjust the import based on your structure

# Create all tables in the database
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")