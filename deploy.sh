#!/bin/bash

USER="ewok"
HOST="95.213.200.78"
PROJECT_ROOT="/srv/ewok"

rsync -zav --delete --exclude=".*" --exclude="run" --exclude=env --exclude="*.pyc" . ${USER}@${HOST}:${PROJECT_ROOT} || exit 1

ssh root@${HOST} /srv/ewok/env/bin/pip install -r ${PROJECT_ROOT}/requirements.txt || exit 1
ssh root@${HOST} /srv/ewok/env/bin/python ${PROJECT_ROOT}/manage.py migrate || exit 1
ssh root@${HOST} systemctl reload ewok
ssh root@${HOST} journalctl -xafu ewok
