#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn --worker-class=gevent --workers=3 --worker-connections=1000 config.wsgi:application --bind=0.0.0.0:8000 --log-level=DEBUG
