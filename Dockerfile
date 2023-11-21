# start docker with kernal slim + install python 3.11
FROM python:3.11.6-slim-bullseye

# option linux : python
ENV PYTHONUNBUFFERED = 1

# update linux
RUN apt-get update