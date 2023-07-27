# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app, requirements, and run file into the container
COPY app /app/app
COPY requirements.txt /app
COPY run.py /app

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Set the PYTHONPATH to include the current directory
ENV PYTHONPATH=/app

# Run the script.py to use the FastAPI app
CMD ["python", "run.py"]