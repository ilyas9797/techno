#!/usr/bin/env bash
sudo /etc/init.d/mysql start
mysql -p -u root -e "CREATE DATABASE app1db;"
mysql -p -u root -e "CREATE USER dbadmin1@localhost;"
mysql -p -u root -e "GRANT ALL ON app1db.* TO 'dbadmin1'@'localhost';"
python ./manage.py makemigrations
python ./manage.py migrate