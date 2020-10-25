#!/bin/bash
cp index.html.template index.html
hostname=$(echo $(hostname))
sed -i -e 's/SERVER_HOSTNAME/'$hostname'/g' index.html
