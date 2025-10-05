#!/usr/bin/env bash
set -e
python manage.py migrate
gunicorn medicab.wsgi:application -b 0.0.0.0:8000 -w 3
