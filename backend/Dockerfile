# Use the official Python image from Docker Hub
FROM python:3.12-slim

# Install build dependencies, including distutils and git
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-distutils \
    python3-dev \
    git \
    ffmpeg \
    libsndfile1-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
