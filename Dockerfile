# Use an official Python runtime
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (helps with caching)
COPY requirements.txt .

# Install dependencies without cache for smaller images
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 8080 (Cloud Run uses 8080 internally)
EXPOSE 8080

# Run the Dash app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:server"]
