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
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN poetry install --only main

# Copy the application code
COPY ai /app/ai

# Expose port 8000
EXPOSE 8000