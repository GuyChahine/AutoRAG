# Use an official Python image as a base
FROM python:3.11-slim

# Set environment variables
ENV POETRY_VIRTUALENVS_IN_PROJECT=1

# Install Poetry
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && pip install poetry

# Set the working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock README.md /app/

RUN mkdir -p /app/backend && touch /app/backend/__init__.py

# Install dependencies using Poetry
RUN poetry install --only main

# Copy the application code
COPY backend /app/backend

# Expose port 8000
EXPOSE 8000