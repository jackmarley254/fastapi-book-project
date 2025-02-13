# Step 1: Use an official Python image as the base image
FROM python:3.12-slim

# Step 2: Set environment variables to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Step 3: Set the working directory in the container
WORKDIR /app

# Step 4: Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Step 5: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the rest of the application code into the container
COPY . /app/

# Step 7: Expose the required port (FastAPI default port is 8000)
EXPOSE 8000

# Step 8: Set the entry point to run Uvicorn with the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
