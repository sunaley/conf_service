#!/bin/bash
set -e

test -n "${LISTEN_ADDRESS}" || export LISTEN_ADDRESS=0.0.0.0
test -n "${LISTEN_PORT}" || export LISTEN_PORT=8000

gunicorn \
    --preload \
    --bind $LISTEN_ADDRESS:$LISTEN_PORT \
    main:__hug_wsgi__
