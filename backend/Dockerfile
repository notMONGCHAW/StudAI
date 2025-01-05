# Dockerfile
FROM python:3.9-slim

# Install system dependencies and clean up
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the requirements.txt file
COPY backend/requirements.txt .

COPY ./backend /app

COPY ./alembic.ini /app/alembic.ini

COPY ./migrations /app/migrations
# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install PyTorch
RUN pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu

# Install other dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code


# Expose the port the app runs on
EXPOSE 8000

# Command to run the application with Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]