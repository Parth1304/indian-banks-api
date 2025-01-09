FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables
# Ensure Python output is displayed in real time
ENV PYTHONUNBUFFERED=1

# Load environment variables from the .env file
# NOTE: Alternatively, use Docker Compose for managing .env variables
ENV FLASK_ENV=production

# Run the application
CMD ["python", "app.py"]
