# Use a minimal Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Default command (in CI this just verifies the container builds)
CMD ["python3", "main.py"]
