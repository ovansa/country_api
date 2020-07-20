#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/ovansa/country_api.git'

PROJECT_BASE_PATH='/usr/local/apps/country_api'

echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv python-pip-whl supervisor nginx git postgresql-client gcc libc6-dev linux-headers-5.4.0-42-generic postgresql-server-dev-10

# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
python3 -m venv $PROJECT_BASE_PATH/env

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Configure supervisor
cp $PROJECT_BASE_PATH/deploy/supervisor_country_api.conf /etc/supervisor/conf.d/country_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart country_api

# Configure nginx
cp $PROJECT_BASE_PATH/deploy/nginx_country_api.conf /etc/nginx/sites-available/country_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/country_api.conf /etc/nginx/sites-enabled/country_api.conf
systemctl restart nginx.service

echo "DONE! :)"
