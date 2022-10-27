#!/bin/bash

#debug
DEBUG="true"
#DEBUG="false"

#clean up and old files before running 
sudo salt \* cmd.run "sudo rm -rf /tmp/tests"
sudo salt \* cmd.run "sudo rm -rf /tmp/network-test-ip-addresses.json"

#generate the current list of hosts and interfaces in json and ship to all hosts
echo "generating a list of current hosts and interfaces"
sudo salt -t 60 --out json '*' network.ip_addrs > /tmp/network-test-ip-addresses.json
sudo salt \* cmd.run "mkdir -p /tmp/tests"
sudo salt-cp --chunked '*' /tmp/network-test-ip-addresses.json /tmp/tests/

#ship jq up as its missing and these nodes are isolated. use scp as salt-cp is slow
echo "shipping jq-linux64 to the nodes"
for NODE in $(bin/jq-linux64 -r ". | keys" /tmp/tests/network-test-ip-addresses.json | grep "\"" | sed 's|[" ]||g'); 
do
        if [ "$DEBUG" = true ] ; then
                echo "==================="
                echo "DEBUG: NODE is $NODE"
                echo "==================="
        fi
	if [[ $NODE == *"-master" ]] ; then
		NODE="master" 
	fi
	scp bin/jq-linux64  support@$NODE:/tmp/jq-linux64
done
sudo salt \* cmd.run "mv /tmp/jq-linux64 /usr/local/sbin/jq-linux64"
sudo salt \* cmd.run "chmod a+x /usr/local/sbin/jq-linux64"

#ship up the test scripts
echo "shipping the test scripts to the nodes"
sudo salt-cp --chunked '*' /home/support/mop-remove-vswitches/bin/test* /tmp/tests/

#execute test1 on the master
sudo salt "nokia-deepfield-master" cmd.run "/tmp/tests/test1.sh"

#execute test2 on each node and run it 
sudo salt \* cmd.run "/tmp/tests/test2.sh"

#execute test3 on each node and run it 
sudo salt \* cmd.run "/tmp/tests/test3.sh"

#clean up 
sudo salt \* cmd.run "sudo rm -rf /tmp/tests"
sudo salt \* cmd.run "sudo rm -rf /tmp/network-test-ip-addresses.json"


