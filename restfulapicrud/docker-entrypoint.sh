#!/bin/bash

# Installing requirements
echo "Installing requirements"
pip install -r requirements.txt

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000