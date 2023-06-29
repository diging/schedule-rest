#!/bin/sh

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

export STATIC_URL='/scheduler/static/'
gunicorn --bind=0.0.0.0 sched.wsgi