#!/bin/bash

cp /var/app/index.html.template /var/app/index.html
hostname=$(echo $(hostname))
sed -i -e 's/SERVER_HOSTNAME/'$hostname'/g' /var/app/index.html
python3 -m http.server 8080 --directory /var/app


