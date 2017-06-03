#!/usr/bin/env bash
sudo /etc/init.d/mysql start
mysql -p -u root -e "CREATE DATABASE appdb;"
mysql -p -u root -e "CREATE USER dbadmin@localhost;"
mysql -p -u root -e "GRANT ALL ON appdb.* TO 'dbadmin'@'localhost';"
python ./manage.py makemigrations
python ./manage.py migrate