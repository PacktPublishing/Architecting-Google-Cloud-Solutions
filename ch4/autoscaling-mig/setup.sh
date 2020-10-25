#!/bin/bash

mkdir /var/app
cp index.html.template /var/app/
cp start_webserver.sh /var/app/

#crontab -e
@reboot /var/app/start_webserver.sh
