# start docker with kernal slim + install python 3.11
FROM python:3.11.6-slim-bullseye

# option linux : python
ENV PYTHONUNBUFFERED = 1

# update linux
RUN apt-get update && apt-get -y install gcc libpq-dev #لمساعدة تنزيل المكتبابالمبنية بالبايث

# create folder ----> project
WORKDIR /app


#  pip freeze > requirements.txt



