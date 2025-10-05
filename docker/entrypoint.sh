#!/usr/bin/env bash
set -e
bash docker/wait_for.sh db:5432
bash docker/wait_for.sh minio:9000
python manage.py migrate
python manage.py collectstatic --noinput || true
gunicorn medicab.wsgi:application -b 0.0.0.0:8000 -w 3
