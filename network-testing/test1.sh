#!/bin/bash

echo "************************************************************"
echo "Test1: HOST ${HOSTNAME} : ping between all hosts in the private link using salt"
echo "************************************************************"
sudo salt -t 60 \* test.ping
