# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the Flask API will run
EXPOSE 5000

# Set the command to run the Flask API
CMD ["flask", "run", "--host", "0.0.0.0"]