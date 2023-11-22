# start docker with kernal slim + install python 3.11
FROM python:3.11.6-slim-bullseye

# option linux : python
ENV PYTHONUNBUFFERED = 1

# update linux #لمساعدة تنزيل المكتباب المبنية بالبايث gcc
RUN apt-get update && apt-get -y install gcc libpq-dev 

# create folder ----> project
WORKDIR /app

# pip freeze > requirements.txt

# copy requirements.txt file
COPY requirements.txt /app/requirements.txt

# install all libraries # -r read
RUN pip install -r /app/requirements.txt 

# copy all project files
COPY . /app/

