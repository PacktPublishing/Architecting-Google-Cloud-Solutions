#!/bin/bash

mkdir /var/app
cp index.html.template /var/app/
cp start_webserver.sh /var/app/
chmod +x /var/app/start_webserver.sh

(crontab -l; echo "@reboot /var/app/start_webserver.sh") | crontab -
