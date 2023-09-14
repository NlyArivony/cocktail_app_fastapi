# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app, requirements, and run file into the container
COPY app /app/app
COPY requirements.txt /app
COPY main.py /app
COPY run.py /app
# COPY .env /app

# Install PostgreSQL development packages and gcc
RUN apt-get update && apt-get install -y libpq-dev gcc

# Install Vim
RUN apt-get install -y vim

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Set the PYTHONPATH to include the current directory
ENV PYTHONPATH=/app

# Run the script.py to use the FastAPI app
CMD ["python", "run.py"]
