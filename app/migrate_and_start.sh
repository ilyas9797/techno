#!/usr/bin/env bash
sudo /etc/init.d/mysql start
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py runserver