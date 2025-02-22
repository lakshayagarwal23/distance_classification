# Use the official Python 3.11 image as the base
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Set the default command to run your script
CMD ["python", "distance_classification.py"]
