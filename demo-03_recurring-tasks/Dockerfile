FROM python:3.8.12-slim

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./app ./app
COPY requirements.txt .
RUN pip install -r requirements.txt

