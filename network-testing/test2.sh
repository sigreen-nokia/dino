#!/bin/bash

#debug
#DEBUG="true"
DEBUG="false"

echo "************************************************************"
echo "Test2: HOST ${HOSTNAME} ping between all hosts on all like interfaces using mtu=1500"
echo "************************************************************"

if [ "$DEBUG" = true ] ; then
    echo "DEBUG: dump array of hosts and interfaces"
    echo "==================="
    echo ${HostInterfaces[@]}
    echo "==================="
fi
if [ "$DEBUG" = true ] ; then
    echo "DEBUG: dump /tmp/tests/network-test-ip-addresses.json"
    echo "==================="
    cat /tmp/tests/network-test-ip-addresses.json 
    echo "==================="
fi

for NODE in $(/usr/local/sbin/jq-linux64 -r ". | keys" /tmp/tests/network-test-ip-addresses.json | grep "\"" | sed 's|[" ]||g'); 
do
	if [ "$DEBUG" = true ] ; then
    		echo "==================="
    	   	echo "DEBUG: NODE is $NODE"
    		echo "==================="
	fi
	echo "************************************************************"
	echo "Testing from ${HOSTNAME} to $NODE mtu 1450"
	echo "************************************************************"
	for IP in $(/usr/local/sbin/jq-linux64 -r "try .\"$NODE\"[]" /tmp/tests/network-test-ip-addresses.json);
	do
		if [ "$DEBUG" = true ] ; then
    	   		echo "DEBUG: IP is $IP"
		fi
		echo "-------------------------------"
		echo "ping -c 1 -s 1450 -c1 -M do $IP"
		ping -c 1 -s 1450 -M do $IP > /dev/null
	   	if [ $? -ne 0 ]; then	
    		  	echo "ERROR: PING FAILED"
		else
			echo "PASS"
  		fi
	done
done

