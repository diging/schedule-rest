#!/bin/sh

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

source .env
gunicorn --bind=0.0.0.0 sched.wsgi