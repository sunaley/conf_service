#!/bin/bash
set -e

WORK_DIR=$IMAGE_PROJECT_DIR
PYTHON=/usr/bin/python3.6
USER_NAME=$1
USER_ID=$2

rsync -avh \
    /tmp/project/ $WORK_DIR

groupadd -r $USER_NAME -g $USER_ID && useradd -m -g $USER_NAME $USER_NAME -u $USER_ID

chown -R $USER_ID:$USER_ID $(dirname $WORK_DIR)