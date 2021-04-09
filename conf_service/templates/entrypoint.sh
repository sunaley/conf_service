#!/bin/bash
set -e

WORK_DIR=$IMAGE_PROJECT_DIR
PYTHON=/usr/bin/python3.6
GOSU=/usr/local/bin/gosu
USER_NAME=$1
USER_ID=$2

{% if migrate -%}
$GOSU $USER_ID $PYTHON manage.py migrate
{% endif -%}
{% if collectstatic -%}
$GOSU $USER_ID $PYTHON manage.py collectstatic --no-input
{% endif -%}
{% if timedrive -%}
$GOSU $USER_ID $PYTHON bin/{{ timedrive_name }}
{% endif -%}
{% if filedrive -%}
$GOSU $USER_ID $PYTHON bin/{{ filedrive_name }}
{% endif %}

$GOSU $USER_ID /usr/local/bin/gunicorn \
    --preload \
    --bind 0.0.0.0:8080 {{ project }}.wsgi \
    --error-logfile $WORK_DIR/logfiles/gunicorn.error.log \
    --access-logfile $WORK_DIR/logfiles/gunicorn.access.log \
    --timeout 360 --workers 3 --max-requests 10000
