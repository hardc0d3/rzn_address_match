# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt --no-cache
