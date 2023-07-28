# Pull base image
FROM python:3.10.2-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /eco2ai_playground/

COPY . /eco2ai_playground/

# Install dependencies
RUN pip install poetry
RUN poetry install

EXPOSE 8000
