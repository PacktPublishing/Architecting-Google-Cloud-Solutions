#!/bin/bash

cp /var/app/index.html.template /var/app/index.html
hostname=$(echo $(hostname))
sed -i -e 's/SERVER_HOSTNAME/'$hostname'/g' /var/app/index.html
cd /var/app
python3 webserver.py &


