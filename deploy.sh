#!/bin/bash -e

USER="ewok"
HOST="95.213.200.78"
PROJECT_ROOT="/srv/ewok"

rsync -zav \
    --delete \
    --exclude=".*" \
    --exclude="run" \
    --exclude="deploy.sh" \
    --exclude=env \
    --exclude="*.pyc" \
    . ${USER}@${HOST}:${PROJECT_ROOT}

ssh root@${HOST} /srv/ewok/env/bin/pip install -r ${PROJECT_ROOT}/requirements.txt
ssh root@${HOST} /srv/ewok/env/bin/python ${PROJECT_ROOT}/manage.py collectstatic --noinput
ssh root@${HOST} /srv/ewok/env/bin/python ${PROJECT_ROOT}/manage.py migrate
ssh root@${HOST} systemctl reload ewok
ssh root@${HOST} journalctl -xafu ewok
