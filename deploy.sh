#!/bin/bash

USER="ewok"
HOST="95.213.200.78"
PROJECT_ROOT="/srv/ewok"

rsync -zav --delete --exclude=".*" --exclude="run" --exclude=env --exclude="*.pyc" . ${USER}@${HOST}:${PROJECT_ROOT}

ssh root@${HOST} systemctl reload ewok
ssh root@${HOST} journalctl -xafu ewok
