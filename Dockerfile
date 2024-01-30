FROM python:3.9-slim-buster

# Create and set the working directory in the container
RUN mkdir /app
WORKDIR /app

# set environment variables
# Prevents Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1


# Setup GDAL
RUN apt-get update &&\
   apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal 

# upgrade pip version
RUN pip install --upgrade pip

# copy requirements to the image
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# Copy over the project
COPY . /app


ENTRYPOINT ["gunicorn","core.wsgi"]