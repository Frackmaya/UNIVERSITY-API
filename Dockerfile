# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /UNIVERSITY-API

#  from root of your current folder
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app code
COPY . .


# Expose port
EXPOSE 8000

# Run the Flask app
CMD ["python", "UNIVERSITY-API/app.py"]

