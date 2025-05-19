# Use a minimal Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Default command to verify build
CMD ["python3", "main.py"]
