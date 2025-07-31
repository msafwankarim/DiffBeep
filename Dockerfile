# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and source code
COPY requirements.txt ./
COPY main.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Entrypoint
CMD ["python","-u", "main.py"]
