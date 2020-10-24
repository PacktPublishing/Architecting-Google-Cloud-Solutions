#!/bin/bash
hostname=$(echo $(hostname))
sed -i -e 's/SERVER_HOSTNAME/'$hostname'/g' index.html
