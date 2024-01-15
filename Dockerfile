# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY ./Content /usr/lib/aptlyws/Content
COPY ./images  /usr/lib/aptlyws/images
COPY ./Model /usr/lib/aptlyws/Model
COPY ./templates /usr/lib/aptlyws/templates
COPY ./aptly_wa /app/aptly_wa

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Make port 80 available to the world outside this container
EXPOSE 8090

# Define environment variable
ENV PAGE_TEMPLATES /usr/lib/aptlyws/templates
ENV PAGE_IMAGES /usr/lib/aptlyws/images
ENV PAGE_CONTENT /usr/lib/aptlyws/Content
ENV PAGE_API /usr/lib/aptlyws/api
ENV UI_FAVICON aptly-icon3x.png
ENV UI_BIND_ADDRESS 0.0.0.0
ENV UI_PORT 8090
ENV API_APTLY_URL http://localhost:8080/api

# Run app.py when the container launches
CMD ["python3", "app.py"]