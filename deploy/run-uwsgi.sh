#!/bin/sh

set -ex

python3 manage.py migrate
python3 load_initial_data.py
exec uwsgi --ini /srv/app/deploy/uwsgi.ini
