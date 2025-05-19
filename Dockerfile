# Use a minimal Python image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Default command (runs your calculator)
CMD ["python3", "main.py"]
