#!/bin/bash

sed -i -e 's/SERVER_HOSTNAME/$(hostname)/g' index.html
