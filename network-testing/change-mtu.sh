#!/bin/bash

############################################################
# Help                                                     #
############################################################
Help()
{
   # Display Help
   echo "change-mtu.sh: run on the master and it will set the mtu on all interfaces on all nodes"
   echo "               the mtu is changed dynamically (does not require  reboot) and statically (will be maintained across a reboot)"
   echo
   echo "Example Syntax: change-mtu.sg -m 1500"
   echo "Example Syntax: change-mtu.sg -m 9000"
   echo "options:"
   echo "m [value] 	change mtu on all nodes"
   echo "d     		dump mtu on all nodes"
   echo "h     		Print this Help."
   echo "v     		Print software version and exit."
   echo
}

Version()
{
   # Display version
   echo "Version 1.0"
}

MtuChange()
{


if [[ -z "$MTU" ]]; then
    echo "ERROR: MTU not specified -m [value]" 1>&2
    exit
fi

echo "The mtu's are currently set as follows" 
sudo salt \* cmd.run "ifconfig -a | grep -i mtu"
echo "and in /etc/network/interfaces"
sudo salt \* cmd.run "sudo cat /etc/network/interfaces | grep -i mtu"

echo "dyamically setting mtu to $MTU on all nodes" 
sudo salt \* cmd.run "for i in \`ip -o link show | awk -F': ' '{print \$2}' | grep -v lo\`; do sudo ip link set dev \$i mtu $MTU; done"

echo "statically setting mtu to $MTU on all nodes" 
sudo salt \* cmd.run "sed -i 's/mtu \\([0-9]\\+\\)/mtu $MTU/g' /etc/network/interfaces"

echo "The mtu's are now set as follows" 
sudo salt \* cmd.run "ifconfig -a | grep -i mtu"
echo "and in /etc/network/interfaces"
sudo salt \* cmd.run "sudo cat /etc/network/interfaces | grep -i mtu"
}

MtuDump()
{
echo "The mtu's are currently set as follows" 
sudo salt \* cmd.run "ifconfig -a | grep -i mtu"
echo "and in /etc/network/interfaces"
sudo salt \* cmd.run "sudo cat /etc/network/interfaces | grep -i mtu"
}


############################################################
############################################################
# Main program                                             #
############################################################
############################################################
############################################################
# Process the input options. Add options as needed.        #
############################################################
# Get the options
while getopts ":hvdm:" option; do
   case $option in
      h) # display Help
         echo "Help"
         Help
         exit
	 ;;
      v) # display version 
         Version 
         exit
	 ;;
      d) # dump mtu
         echo "Dumping MTU on all nodes"
	 MtuDump
	 exit
	 ;; 
      m) # change mtu
         echo "Setting MTU on all nodes"
         MTU=$OPTARG
	 MtuChange
	 exit
	 ;; 
      *)              
         echo "Error: Invalid option"
         exit         
         ;;
      \?)
         echo "Error: Invalid option"
         exit
	 ;;
   esac
done

Help
