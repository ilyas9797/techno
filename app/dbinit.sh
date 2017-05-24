#!/usr/bin/env bash
sudo /etc/init.d/mysql start
mysql -p -u root -e "CREATE DATABASE taskdb;"
mysql -p -u root -e "CREATE USER dbuser@localhost;"
mysql -p -u root -e "GRANT ALL ON taskdb.* TO 'dbuser'@'localhost';"
python ./manage.py makemigrations
python ./manage.py migrate