FROM python:3.10.0-slim-buster
LABEL maintainer="luitko007@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

USER django-user
