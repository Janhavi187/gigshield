FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for psycopg2 & geospatial libs
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose API port
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
