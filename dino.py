# importing the modules
#To add missing modues: 
#                       pip install [module name]: 
#                       or 
#                       pip3 install [module name]: 
import os
import sys 
import re
import subprocess
import socket
import json 
import csv 
import time
from subprocess import check_output as run
from datetime import date
from pathlib import Path
RunningOnMaster = "yes"
#requests is a must have and is available with pip/pip3
try:
    import requests 
except ImportError:
    print ("\nPlease Install python module requests using")
    print ("       'pip install requests'")
    print ("       or")
    print ("       'pip3 install requests'")
    print ("Then rerun dino\n")
    sys.exit(1) 
#test for these modules to determine whether we are running on a master of a customers node
try:
    import deepy.cfg
except ImportError:
    RunningOnMaster = "no"
try:
    import deepy.deepui
except ImportError:
    RunningOnMaster = "no"
try:
    import get_context
except ImportError:
    RunningOnMaster = "no"
try:
    import pandas as pd
except ImportError:
    RunningOnMaster = "no"
try:
    import deepy.log as log
except ImportError:
    RunningOnMaster = "no"
try:
    from deepy.encryption_utils import EncryptFile
except ImportError:
    RunningOnMaster = "no"
#date 
today = str(date.today())
#statics
logDir = '/pipedream/log/'
uiLogName = 'ui.log'
#data_view_size_logging
disk_space_filename=Path("data_view_disk_space.csv")
disk_space_filename_sorted=Path("data_view_disk_space_sorted.csv")
# path to place the dino working files directory
# WorkingDir = '/tmp'
WorkingDir = '/pipedream/log/'
# log of all queries
queriesFile = './queries_from_logs.txt'
# results files with query-counts and sorted query-counts 
querySummaryfile = 'querysummary.csv'
querySummaryfileSorted = 'querysummary_sorted_on_count.csv'
# Define Regex paterns to extract query-fields
# type (cube or count) query
type_regex = re.compile(r"/(cube|count)/")
# pattern to ID cube and the dimensions
cube_regex = re.compile(r"cube/(\w*)\.")
# pattern to ID cube and the dimensions
dim_regex = re.compile(r"dimensions=([\w,.-]*)&")
# pattern to ID the timestamp slice
timestamp_regex = re.compile(r"slice=timestamp([\w\-:()]*)&?")
# pattern to ID the dimensions in slice
slice_regex = re.compile(r"slice=([\w.\-]*)&?")
# pattern to ID the APIkey
apikey_regex = re.compile(r"api_key=([\w,.-]*)&?")
# pattern to ID the boundary slice
boundaryslice_regex = re.compile(r"bs=\(([\w,-.()]*)\)&?")
# pattern to extract each boundary from the boundary slice
boundary_regex = re.compile(r"\((boundary\.[\w.-]*),.*\)")
# api_key
api_key = 'None' 

def topmenu():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDino - Deepfield customer engineer trainer")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")

    while True:
        print("""
            1.Whats a trainer ? 
            2.Deepfield Example Queries (empty) 
            3.Deepfield Cluster Health
            4.Deepfield Cluster Configuration 
            5.Queries the customer is using most frequently (view optimization, thanks ato)
            6.mysql (not used anymore)
            7.postgres
            8.impala (empty)
            9.kafka
            10.redis (empty)
            11.tracing (empty)
            12.networking and bonding
            13.bgp (empty)
            14.MOP
            15.HDFS
            16.Devices API, Routers and Interfaces
            17.Data Views
            18.Backup config, logs, etc
            19.Defender (DDoS)
            20.Dimensions
            21.Organizations and Users
            22.Boundaries
            23.Exit""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            whatsatrainer()    
        elif ch == 2:
            submenu22()    
        elif ch == 3:
            submenu23()    
        elif ch == 4:
            submenu24()    
        elif ch == 5:
            submenu25() 
        elif ch == 6:
            print("mysql is not longer used in Deepfield, the sub menu has been removed, see the postgres menu")
            input("Press any key to return to the menu")
            topmenu()
        elif ch == 7:
            submenu27() 
        elif ch == 8:
            os.system("systemctl status httpd")
        elif ch == 9:
            submenu29() 
        elif ch == 10:
            new_user=input("Enter the name of new user: ")
            os.system("sudo useradd {}".format(new_user))
            os.system("id -u {}".format(new_user) )
        elif ch == 11:
            del_user=input("Enter the name of the user to delete: ")
        elif ch == 12:
            submenu212() 
        elif ch == 13:
            foldername=input("Enter the foldername: ")
        elif ch == 14:
            submenu214() 
        elif ch == 15:
            submenu215() 
        elif ch == 16:
            submenu216() 
        elif ch == 17:
            submenu217() 
        elif ch == 18:
            submenu218() 
        elif ch == 19:
            submenu219() 
        elif ch == 20:
            submenu220() 
        elif ch == 21:
            submenu221() 
        elif ch == 22:
            submenu222() 
        elif ch == 23:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        topmenu()

def submenu22():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Example Queries")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Traffic: 
            2.Sub-i: 
            3.DDoS:
            4.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            os.system("ls")
        elif ch == 2:
            os.system("ls")
        elif ch == 3:
            os.system("ls")
        elif ch == 4:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu22

def submenu23():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Cluster Health (must be ran on the master)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.salt-ping all nodes                      			#tests basic connectivity Master to each worker
            2.soup status on all nodes      		       		#checks the status of the Deepfield processes
            3.check disk space 						#show disk space available per partition for all nodes    
            4.memory hogs 						#show the top processes consuming memory for all nodes 
            5.check the performance of dnsflowd on each worker 	        #100% indicated it is time to scale up
            6.check the performance of classifyd on each worker 	#100% indicated it is time to scale up
            7.check the performance of collectd on each worker 	        #100% indicated it is time to scale up
            8.check the performance of normd on each worker 	        #100% indicated it is time to scale up
            9.cpu hogs 							#show the top processes consuming cpu for all nodes 
            10.show me the cpu details for each node 			#cpu details
            11.show me the cpu model for each node 			#cpu model
            12.get the cpu clock speeds for each node 			#wondering why one node is busy.. perhaps you have a fan out and the clock was stepped
            13.Whats taking up all my SWAP space
            14.How much SWAP space do I have
            15.flow                                                     #show router flow per DCU
            16.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycmd = "sudo salt \* test.ping"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 2:
            mycmd = "sudo salt \* cmd.run \"supervisorctl status\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 3:
            mycmd = "sudo salt \* cmd.run \"df -h\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 4:
            mycmd = "sudo salt \* cmd.run \"ps -eo %mem,%cpu,pid,ppid,cmd --sort=-%mem | cut -c -140 | head -n 20 \""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 5:
            mycmd = "sudo salt \* cmd.run \"ps -eo %mem,%cpu,pid,ppid,cmd --sort=-%mem | cut -c -140 | grep dnsflow | grep -v grep \""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 6:
            mycmd = "sudo salt \* cmd.run \"ps -eo %mem,%cpu,pid,ppid,cmd --sort=-%mem | cut -c -140 | grep classifyd | grep -v grep \""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 7:
            mycmd = "sudo salt \* cmd.run \"ps -eo %mem,%cpu,pid,ppid,cmd --sort=-%mem | cut -c -140 | grep collectd | grep -v grep \""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 8:
            mycmd = "sudo salt \* cmd.run \"ps -eo %mem,%cpu,pid,ppid,cmd --sort=-%mem | cut -c -140 | grep normd | grep -v grep \""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 9:
            mycmd = "sudo salt \* cmd.run \"ps -eo %mem,%cpu,pid,ppid,cmd --sort=-%cpu | cut -c -140 | head\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 10:
            mycmd = "sudo salt \* cmd.run \"lscpu\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 11:
            mycmd = "sudo salt \* cmd.run \"lshw | grep -i intel | grep -i cpu\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 12:
            mycmd = "sudo salt \* cmd.run \"cat /proc/cpuinfo | grep MHz\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 13:
            mycmd = ("for file in /proc/*/status ; do awk '/VmSwap|Name/{printf $2 \" \" $3}END{ print \"\"}' $file; done | sort -k 2 -n -r")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 14:
            mycmd = ("grep -i swap /proc/meminfo")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 15:
            mycmd = ("flow.py --show-realtime")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 16:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu23()

def submenu24():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Cluster Configuration (must be ran on the master)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.salt roles configured on each node 			#shows the configured services on each node 
            2.who has the dnsflow salt role     			#which dcu's
            3.who has the collector salt role     			#which dcu's
            4.List all configured routers
            5.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycmd = "sudo salt \* grains.get roles"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 2):
            mycmd = "sudo salt -G roles:dnsflow test.ping"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 3):
            mycmd = "sudo salt -G roles:collector test.ping"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 4):
            mycmd = "routers.py --list | tr -s ' '"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 5:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu24()

def submenu25():
    os.system("clear")
    #set the context as a global
    global mycontext 
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Queries the customer is using most frequently (view optimization, must be ran on the master)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Show the most frequently ran customer queries in context traffic 
            2.Show the most frequently ran customer queries in contexts backbone
            3.Show the most frequently ran customer queries in contexts big_cube 
            4.Show the most frequently ran customer queries in context subscriber
            5.Show the most frequently ran customer queries in context video_stream
            6.Show the most frequently ran customer queries in context flowdump
            7.Cleanup the dino-* directories used to store the queries
            8.Return""")
        print("\n")
        #to get available cubes https://localhost:22222/cube/list
        ch=int(input("Enter your choice: "))
        # you can list more than one context, coma seperated
        if(ch == 1):
            mycontext = ['traffic'] 
            getMostUsedQueries()
        elif ch == 2:
            mycontext = ['backbone'] 
            getMostUsedQueries()
        elif ch == 3:
            mycontext = ['big_cube'] 
            getMostUsedQueries()
        elif ch == 4:
            mycontext = ['subscriber'] 
            getMostUsedQueries()
        elif ch == 5:
            mycontext = ['video_stream'] 
            getMostUsedQueries()
        elif ch == 6:
            mycontext = ['flowdump'] 
            getMostUsedQueries()
        elif ch == 7:
            os.system("rm -rf " + WorkingDir + "dino-*")
        elif ch == 8:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu25()

def submenu27():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tpostgres (must be ran on the master)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.List the databases in postgres using psql
            2.List the relations in a selected database (pending)
            3.Count the entries in a selected database for a selected relation (pending)
            4.Dump the entries in a selected database for a selected relation (pending)
            5.postgres database hints 
            6.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycmd = "sudo -u postgres psql -c '\l'"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 2):
            mycmd = "sudo salt -G roles:dnsflow test.ping"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 3):
            mycmd = "sudo salt -G roles:collector test.ping"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 4):
            mycmd = "routers.py --list | tr -s ' '"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 5):
            print("connect to postgres:             sudo -u postgres psql")
            print("list the databases:              \l")
            print("list the tables:                 \dt")
            print("switch to a new dataabse:        \c \"name\"")
            print("select boundaries:               \d list all tables, views and sequences. \"Boundaries\"")
            print("list ids from boundaries:        select id, name from \"Boundaries\";")
            print("count the active interfaces:     select active, count(*) from \"Interfaces\" group by active;")
            print("quit:                            \q")
            print("run one command and exit:        sudo -u postgres psql -d \"defender_zen-saha\" -c 'select id, name from \"Boundaries\";'")
            print("update an interface:             sudo -u postgres psql -d \"defender_nostalgic-penguin\" -c \"update \\\"Interfaces\\\" set name='test3' where id=2;\"")
        elif ch == 6:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu27()

def submenu218():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tBackup config, logs etc.)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Collect log files and slice.json from all DCUs, make one large tar file on master
            2.Dump all DCU's network configuration to all DCU's to a tar file 
            3.Collect the config via api for Analytics, make one large tar file on master
            4.Clean up old tar files
            5.Generate a config_sync backup, without enabling config sync
            6.Unencrypt a config_sync backup so you can look at its contents
            7.Add a cron to once a week sync the master postgress backups to worker01
            8.Remove the cron to once a week sync the master postgress backups to worker01
            9.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            print("\tCollect the logs and slice.json from all DCUs")
            # sets the text color to magenta
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 1)Cleaning up old tar files")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/log.*.tar.gz || true\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 2)tar'ing and zip'ing up the log files on all DCUs, This could take 10-20 minutes")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt -t 3600 \* cmd.run 'tar czvf /pipedream/tmp/log.`hostname`.tar.gz /var/log/ /pipedream/log/ /pipedream/cache/config/slice.json || true'")
            print("Command is:" + mycmd )
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step3) Setting file permissions")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt \* cmd.run 'chown support:support /pipedream/tmp/log.`hostname`.tar.gz'")
            print("Command is:" + mycmd )
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 4)Copying the files from the workers back to master")
            print("\t-------------------------------------------------")
            mycmd = ("for i in $(awk '{if(/mgmt/ && /worker/){print $1}}' /etc/hosts); do scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q $i:/pipedream/tmp/log.worker*.tar.gz /pipedream/tmp; done")
            print("Command is:" + mycmd )
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 5)tar'ing up the tar files into one big file")
            print("\t-------------------------------------------------")
            mycmd = ("tar cvf /pipedream/tmp/defender-all-logs.tar.gz /pipedream/tmp/log*.tar.gz")
            print("Command is:" + mycmd )
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 6)Clean up")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/log.*.tar.gz || true\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
            os.system("tput setaf 6")
            print("All Done") 
            print("\n\n=====================================================================================================") 
            print("The resultant file /pipedream/tmp/defender-all-logs.tar.gz is going to be large (10-20G in size).") 
            print("move the file to your laptop, example laptop command follows") 
            print("scp [host]/pipedream/tmp/defender-all-logs.tar.gz .") 
            print("then use the next menu option to clean up") 
            print("=====================================================================================================") 
            input("Press enter to return to the menu")
            os.system("clear")
            submenu218() 
        elif(ch == 2):
            print("\tDump all DCU's network configuration to all DCU's to a tar file")
            print("\t-------------------------------------------------")
            print ("Step 1)Cleaning up old tar files")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/network-config* || true\"")
            mycmd = ("sudo rm -f /pipedream/tmp/network-all-files-all-hosts.tar.gz")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 2)tar'ing and zip'ing up the network config files on all DCUs,")
            print("\t-------------------------------------------------")
            mycmd = "sudo salt \* cmd.run \"echo ****ip-addr-show*** > /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"ip addr show | tee -a /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"echo ****ifconfig*** >> /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"ifconfig | tee -a /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"echo ****netstat-rn*** >> /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"netstat -rn | tee -a /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = ("sudo salt -t 3600 \* cmd.run 'tar czvf /pipedream/tmp/network-config.`hostname`.tar.gz /etc/network/interfaces /etc/network/interfaces.d /etc/resolv.conf /etc/hosts /pipedream/tmp/network-config-dynamic-config* || true'")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step3) Setting file permissions")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt \* cmd.run 'chown support:support /pipedream/tmp/network-config.`hostname`.tar.gz'")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 4)Copying the files from the workers back to master")
            print("\t-------------------------------------------------")
            mycmd = ("for i in $(awk '{if(/mgmt/ && /worker/){print $1}}' /etc/hosts); do scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q $i:/pipedream/tmp/network-config.worker*.tar.gz /pipedream/tmp; done")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 5)tar'ing up the tar files into one big file")
            print("\t-------------------------------------------------")
            mycmd = ("tar czvf /pipedream/tmp/network-all-files-all-hosts.tar.gz /pipedream/tmp/network-config.*.tar.gz")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 6)Clean up")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/network-config* || true\"")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 7)Copying the big zip file back out to all the workers")
            print("\t-------------------------------------------------")
            mycmd = ("for i in $(awk '{if(/mgmt/){print $1}}' /etc/hosts); do scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q /pipedream/tmp/network-all-files-all-hosts.tar.gz $i:/home/support/network-all-files-all-hosts.tar.gz; done")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("All Done") 
            print("\n\n=====================================================================================================") 
            print("The resultant file /home/support/network-all-files-all-hosts.tar.gz") 
            print("is on all DCU's and contains every DCU's dynamic and static network configuration") 
            print("=====================================================================================================") 
            input("Press enter to return to the menu")
            os.system("clear")
            submenu218() 
        elif(ch == 3):
            print("-------------------------------------------------")
            print("Collect the config via api for Analytics, make one large tar file on master")
            print("-------------------------------------------------")
            print ("Step 1)Cleaning up old files")
            print("\t-------------------------------------------------")
            mycmd = ("sudo rm -rf /home/support/api-config-backup")
            os.system(mycmd)
            mycmd = ("sudo rm -f /home/support/api-config-backup.tar.gz")
            os.system(mycmd)
            mycmd = ("mkdir /home/support/api-config-backup")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("-------------------------------------------------")
            print ("Step 2)dump the user configuration via the api")
            print("-------------------------------------------------")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/users/?api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/users.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 3)dump the organization configuration via the api")
            print("-------------------------------------------------")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/organization/?api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/organization.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 4)dump the boundaries configuration via the api")
            print("-------------------------------------------------")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/boundaries/?api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/boundaries.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 4)dump the configuration rules via the api")
            print("-------------------------------------------------")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/configuration_rules/?limit=999&api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/configuration_rules.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 5)dump the router dimensions via the api")
            print("-------------------------------------------------")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/dimensions/router?api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/dimensions_router.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 6)dump the router dimension possitions attributes via the api")
            print("-------------------------------------------------")
            #curl --insecure -X GET 'https://localhost/dimension/router/positions?&attributes=(*)&api_key=31UO2fiKwinzYl'
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/dimension/router/positions?&attributes=(*)&api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/dimensions_router_possitions_attributes.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 7)dump the dimensions index via the api")
            print("-------------------------------------------------")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/dimensions/index?api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/dimensions_index.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 8)dump the interfaces dimension possitions attributes via the api")
            print("-------------------------------------------------")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/dimension/interfaces/positions?&attributes=(*)&api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/dimensions_interfaces_possitions.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 9)dump the data_views dimension via the api")
            print("-------------------------------------------------")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/data_views/?api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/dimensions_data_views.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 10)dump the first class dimension via the api")
            print("-------------------------------------------------")
            mycmd = ("echo '**markets***' > /home/support/api-config-backup/dimensions_first_class.json")
            os.system(mycmd)
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/dimensions/markets/positions?api_key=" + API_Key + "' | json_pp >> /home/support/api-config-backup/dimensions_first_class.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            mycmd = ("echo '**pops***' >> /home/support/api-config-backup/dimensions_first_class.json")
            os.system(mycmd)
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/dimensions/pops/positions?api_key=" + API_Key + "' | json_pp >> /home/support/api-config-backup/dimensions_first_class.json")
            os.system(mycmd)
            print("Command is:" + mycmd )
            mycmd = ("echo '**onnet_cache***' >> /home/support/api-config-backup/dimensions_first_class.json")
            os.system(mycmd)
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/dimensions/onnet_cache/positions?api_key=" + API_Key + "' | json_pp >> /home/support/api-config-backup/dimensions_first_class.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            mycmd = ("echo '**vpn***' >> /home/support/api-config-backup/dimensions_first_class.json")
            os.system(mycmd)
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/dimensions/vpn/positions?api_key=" + API_Key + "' | json_pp >> /home/support/api-config-backup/dimensions_first_class.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            mycmd = ("echo '**vpn_site***' >> /home/support/api-config-backup/dimensions_first_class.json")
            os.system(mycmd)
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/dimensions/vpn_site/positions?api_key=" + API_Key + "' | json_pp >> /home/support/api-config-backup/dimensions_first_class.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 11)dump the privacy white list via the api")
            print("-------------------------------------------------")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/privacy/infrastructure-whitelist?api_key=" + API_Key + "' | json_pp > /home/support/api-config-backup/privacy_infrastructure_whitelist.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("-------------------------------------------------")
            print ("Step 12)dump all possitions for all dimensions via the api")
            print("-------------------------------------------------")
            user_input = input("This step will generate a lot of data and take a long time to run. Input yes to run it any other key to skip it:")
            if user_input == 'yes':
                print("\nOk Running it: ")
                url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
                #print ("\nDebug url: " , url)
                dimensionlist = requests.get(url, verify=False).json()
                #print ("\nDebug: Dimensionlist: " , dimensionlist)
                json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
                #print ("\nDebug json_formatted_dimensionlist: " , json_formatted_dimensionlist)
                #build the text menu
                index = 0
                for key in dimensionlist:
                    index += 1
                    #print ("DEBUG: key:", key)
                    dimensionname = dimensionlist[key]['name']
                    dimensionuuid = dimensionlist[key]['dimension_id']
                    #print ("\nDebug: dimensionname: " , dimensionname)
                    #print ("\nDebug: dimensionuuid: " , dimensionuuid)
                    print ("Working on dimension: " , dimensionname)
                    mycmd = ("echo \"Working on dimension name:" + str(dimensionname) + " uuuid:" + str(dimensionuuid) + "\" >> /home/support/api-config-backup/all-dimensions-all-possitions.json") 
                    #print("Debug: Command is:" + mycmd )
                    os.system(mycmd)
                    mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "/positions?&attributes=(*)&api_key=" + API_Key + "' | json_pp >> /home/support/api-config-backup/all-dimensions-all-possitions.json")
                    #print("Debug: Command is:" + mycmd )
                    os.system(mycmd)
                print("\nDone")
            else:
                print ("skipping this step as you did not enter yes")
            print("-------------------------------------------------")
            print ("Step 99)tar'ing up the api dumps into one big tar file")
            print("-------------------------------------------------")
            mycmd = ("tar czvf /home/support/api-config-backup.tar.gz /home/support/api-config-backup/*")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("All Done") 
            print("\n\n=====================================================================================================") 
            print("The resultant file /home/support/api-config-backup.tar.gz") 
            print("Contains the API config dumps") 
            print("=====================================================================================================") 
            input("Press enter to return to the menu")
            os.system("clear")
            submenu218() 
        elif ch == 4:
            print ("Cleaning up old tar files")
            mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/log.*.tar.gz || true\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
            os.system("tput setaf 6")
            mycmd = ("sudo rm -f /pipedream/tmp/defender-all-logs.tar.gz")
            print("Command is:" + mycmd )
            os.system(mycmd)
            os.system("tput setaf 6")
            input("Press any key to return to the menu")
            os.system("clear")
            submenu218() 
        elif ch == 5:
            print ("Generate a config_sync backup, without enabling config sync. Usefull for a rainy day")
            print ("#***You should enable a blackout on slack before you start, just incase you fire a config sync alert")
            print ("#You should also grab a backup of the network configs, its an option in the same menu")
            print ("#the following commands will generate one config_sync backup in directory")
            print ("#/pipedream/cache/config_sync/*")
            print ("#Don't forget to clean up the backup once you have it safe")
            print ("")
            print ("cp /usr/local/sbin/config_sync.py ./custom_config_sync.py")
            print ("")
            print ("#before patching lets check that each of these still finds a match")
            print ("#each of these needs to get a result, else we have to update the patches as the code changed. ")
            print ("grep \"CONFIG_SYNC_ENABLED\" ./custom_config_sync.py")
            print ("grep \"config sync not enabled\" ./custom_config_sync.py")
            print ("grep \"stats.event\" ./custom_config_sync.py")
            print ("grep \"if basename == \\\"slice.json\\\"\" ./custom_config_sync.py")
            print ("grep \"pg_dump_cmd.extend\" ./custom_config_sync.py")
            print ("#all good go ahead and patch our private version")
            print ("sed -i '/CONFIG_SYNC_ENABLED/d' ./custom_config_sync.py")
            print ("sed -i '/config sync not enabled/d' ./custom_config_sync.py")
            print ("sed -i 's/stats.event/#stats.event/g' ./custom_config_sync.py")
            print ("#patch out the slice.json restore code (used later for the recovery)")
            print ("#as we do not want to replace slice.json with the backup ")
            print ("sed -i 's/if basename == \"slice.json\"/if basename == \"not_merging_slice.json\"/g' ./custom_config_sync.py")
            print ("#patch to make sure we backup everything, avoids problems in HealthStatus*")
            print ("sed -i '/pg_dump_cmd.extend/d' ./custom_config_sync.py")
            print ("./custom_config_sync.py -d")
            print ("#you can get the key for encryption/de-cryption with this command")
            print ("grep deployment_encryption_key /pipedream/cache/config/config_sync.json")
            print ("#you can find the config_sync backup files with command")
            print ("ls -lrt /pipedream/cache/config_sync/")
            input("Press any key to return to the menu")
            os.system("clear")
            submenu218() 
        elif ch == 6:
            print ("Unencrypt a config_sync backup so you can look at its contents")
            Config_Sync_File = input("enter the full path to the encrypted config_sync backup file: ")
            if os.path.exists(Config_Sync_File):
                Config_Sync_Key = input("enter the encryption key (hint: /pipedream/cache/config/config_sync.json): ")
                Config_Sync_Decrypted_File = "Decrypted_config_sync_backup.tar.gz"
                with deepy.cfg.store.write_file_atomically(Config_Sync_Decrypted_File) as out_file:
                    try:
                        file_encryption_obj = EncryptFile(Config_Sync_Key.encode("utf8"), Config_Sync_File, out_file)
                        file_encryption_obj.decrypt()
                        print ("All Done.")
                        print ("The original encrypted file was: " + Config_Sync_File)
                        print ("The unencrypted file is here: " + Config_Sync_Decrypted_File)
                        print ("The encryption key was: " + Config_Sync_Key)
                        print ("You can untar the file with the following command:")
                        print ("mkdir decrypted_config_sync")
                        print ("tar zxvf Decrypted_config_sync_backup.tar.gz --directory ./decrypted_config_sync")
                    except:
                        print ("Error decrypting config_sync file: ")
            else:
                print ("Sorry that config_sync backup file does not exist")
            input("Press any key to return to the menu")
            os.system("clear")
            submenu218() 
        elif ch == 7:
            print ("Add a cron to once a week sync the master postgress backups to worker01")
            mycmd = ("sudo printf '#!/bin/sh -e\n#customer requirement: Sync the postgress backup files to worker01, once a week\n/usr/sbin/runuser -l support -c \"ssh worker01 rm -f /pipedream/backup-master/*.sql.gz\"\n/usr/sbin/runuser -l support -c \"/usr/bin/rsync /pipedream/backup/*.sql.gz worker01:/pipedream/backup-master/\"\n' | sudo tee /etc/cron.weekly/postgress-remote-backup")
            #print("Debug: Command is:" + mycmd )
            os.system(mycmd)
            mycmd = ("sudo chmod a+x /etc/cron.weekly/postgress-remote-backup")
            #print("Debug: Command is:" + mycmd )
            os.system(mycmd)
            print ("All done.")
            print ("The cron file has been created here /etc/cron.weekly/postgress-remote-backup")
            print ("*.sql.gz files in /pipedream/backup/ will be synced to /pipedream/backup-master/ on worker01 weekly")
            input("Press enter to continue")
            os.system("clear")
            submenu218() 
        elif ch == 8:
            print ("Remove the cron to once a week sync the master postgress backups to worker01")
            mycmd = ("sudo rm /etc/cron.weekly/postgress-remote-backup")
            #print("Debug: Command is:" + mycmd )
            os.system(mycmd)
            print ("All done.")
            print ("The cron file /etc/cron.weekly/postgress-remote-backup has been remove")
            input("Press enter to continue")
            os.system("clear")
            submenu218() 
        elif ch == 9:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu22
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tCollect the logs and slice.json on all DCUs")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    print ("Cleaning up old log backups")
    mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/log.*.tar.gz || true\"")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("tar and zip up the log files on all DCUs")
    mycmd = ("sudo salt -t 3600 \* cmd.run 'tar czvf /pipedream/tmp/log.`hostname`.tar.gz /var/log/ /pipedream/log/ /pipedream/cache/config/slice.json || true'")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("Setting file permissions")
    mycmd = ("sudo salt \* cmd.run 'chown support:support /pipedream/tmp/log.`hostname`.tar.gz'")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("Copying the files from the workers back to master")
    mycmd = ("for i in $(awk '{if(/mgmt/ && /worker/){print $1}}' /etc/hosts); do scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q $i:/pipedream/tmp/log.worker*.tar.gz /pipedream/tmp; done")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("tar up the tar files")
    mycmd = ("tar cvf /pipedream/tmp/defender-all-logs.tar.gz /pipedream/tmp/log*.tar.gz")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("Clean up")
    mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/log.*.tar.gz || true\"")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print("\n\nThe resultant file /pipedream/tmp/defender-all-logs.tar.gz is going to be large (10-20G in size).") 
    print("move the file to your laptop, example laptop command follows") 
    print("scp [host]/pipedream/tmp/defender-all-logs.tar.gz .") 
    print("then use the next menu option to clean up") 
    input("Press enter to return to the previouse menu")
    os.system("clear")
    topmenu() 

def submenu219():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDefender (DDoS, def.py must be ran on the master. The api's will work locally or remotely)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Build up a def.py report, to gather up the defender configuration and running details
            2.Whats my current running Defender Secure Genome branch version
            3.Get a list of all available Defender Secure Genome versions
            4.Show the Defender Secure Genome version history 
            5.Lookup an ipv4 or ipv6 address in Secure Genome
            6.Read a list of ipv4 or ipv6 addresses and look up each in Secure Genome, output to a file 
            7.Create a custom protection group with ipv4 subnets covering the internet.
            8.Dump the detection rules raw dfmatch in JSON
            9.Dump the mitigation rules raw dfmatch in JSON
            10.Dump the countermeasure dimension positions in JSON
            11.Flip all policies to use flow rather than spm (config-sync use case)
            12.Flip all policies to use spm rather than flow (config-sync use case)
            13.Dump all mitigation devices via the api
            14.Dump all mitigation device groups via the api
            15.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            print ("Building a report of all things Defender for this cluster. Using def.py")
            print ("The result will be written to file DefenderReport.txt")
            mycmd = ("rm -f DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'Defender Summary Status def.py status' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py status | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'Defender Health Report def.py health' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py health | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'All Router Details def.py rt' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py rt | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'All Routers as a list def.py rt --list' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py rt --list | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'Defender Device and interface set list def.py dev --list' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py dev --list | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'Defender Mitigation Template list def.py template --list' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py template --list | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'Defender Policy list def.py policy --list' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py policy --list | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'Defender events def.py event' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py event | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'Defender Mitigation list def.py mitigation --list' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py mitigation --list | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo 'Defender acl list .py def.py acl -l' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("echo '*****************************************************' | tee -a DefenderReport.txt")
            os.system(mycmd)
            mycmd = ("def.py acl -l | tee -a DefenderReport.txt")
            os.system(mycmd)
            input("Press any key to return to the menu")
            os.system("clear")
            submenu219() 
        elif(ch == 2):
            print ("Grabbing your clusters current Secure Genome branch version")
            mycmd = ("curl --insecure -X GET https://" + cluster_fqdn + "/api/secure_genome/version?api_key=" + API_Key + " | json_pp" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
        elif(ch == 3):
            print ("Getting a list of all available secure genome versions")
            mycmd = ("curl --insecure -X GET https://" + cluster_fqdn + "/api/secure_genome/versions?api_key=" + API_Key + " | json_pp" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
        elif(ch == 4):
            print ("Grabbing your clusters Secure Genome version history")
            mycmd = ("curl --insecure -X GET https://" + cluster_fqdn + "/api/secure_genome/history?api_key=" + API_Key + " | json_pp" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
        elif(ch == 5):
            IP_Address = input("Enter an ipv4 or upv6 address to analyse in Secure Genome: ")
            mycmd = ("curl --insecure -X GET https://" + cluster_fqdn + "/api/secure_genome/ip/" + IP_Address + "?api_key=" + API_Key + " | json_pp" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
        elif(ch == 6):
            IP_List_Filename = input("enter the existing filename which contains the list of ipv4 and ipv6 addresses (one address per line): ")
            if os.path.exists("my_ip_list_Genome_Lookups.json"):
               os.remove("my_ip_list_Genome_Lookups.json")
            if os.path.exists(IP_List_Filename):
                with open(IP_List_Filename) as f:
                    for line in f:
                        mycmd = ("curl --insecure -X GET https://" + cluster_fqdn + "/api/secure_genome/ip/" + line.rstrip() + "?api_key=" + API_Key + " | json_pp | tee -a my_ip_list_Genome_Lookups.json" )
                        os.system(mycmd)
                        #print ("DEBUG: line:", line)
                        #print ("DEBUG: Command is:" + mycmd )
                    print ("I've processed the ip list and written the Secure Genome output to  file my_ip_list_Genome_Lookups.json for you")
            else:
                print ("Sorry that file does not exist")
        elif ch == 7:
            print("\n Please look in the Dimensions menu option, for this one.")
        elif(ch == 8):
            print("Dump the detection rules raw dfmatch in JSON")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            #find the detection dimension uuid
            index = 0
            for key in dimensionlist:
                #print ("DEBUG: dimensionname ", dimensionlist[key]['name'])
                if dimensionlist[key]['name'] == "detection":
                    dimensionuuid = dimensionlist[key]['dimension_id']
                    dimensionname = dimensionlist[key]['name']
            print ("dimension name:", dimensionname)
            print ("dimension id:", dimensionuuid)
            print ("Grabbing the detection rules JSON")
            url = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/positions?attribures=match,enabled&api_key=' + API_Key
            #print ("\nDEBUG: url: " , url)
            positionlist = requests.get(url, verify=False).json()
            #print ("\nDEBUG: positionlist: " , positionlist)
            json_formatted_positionlist = json.dumps(positionlist, indent=2)
            #print ("\nDEBUG: json_formatted_positionlist: " , json_formatted_positionlist)
            #for each position id in the selected dimension dump the details
            print ("This will be a big list, so I will also write it to file detection_rules.txt")
            print ("An example api query for one detection rules position looks like this.")
            print ("Where x is each positions id in the dimension")
            print ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "/position/x?attribures=match,enabled&api_key=" + API_Key + "' | json_pp")
            print ("I'll extract the list of rules and dump each one for you")
            input("Press any key to continue...")
            with open('detection_rules.txt', 'w') as f:
                for key in positionlist:
                    #print ("\nDEBUG: key: " , key)
                    url2 = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/position/' + str(key) + '?attribures=match,enabled&api_key=' + API_Key
                    positiondetails = requests.get(url2, verify=False).json()
                    json_formatted_positiondetails = json.dumps(positiondetails, indent=2)
                    print (json_formatted_positiondetails)
                    f.write(str(json_formatted_positiondetails))
            print ("Output was also write it to file detection_rules.txt")
        elif(ch == 9):
            print("Dump the mitigation rules raw dfmatch in JSON")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            #find the mitigation dimension uuid
            index = 0
            for key in dimensionlist:
                #print ("DEBUG: dimensionname ", dimensionlist[key]['name'])
                if dimensionlist[key]['name'] == "mitigation_rule":
                    dimensionuuid = dimensionlist[key]['dimension_id']
                    dimensionname = dimensionlist[key]['name']
            print ("dimension name:", dimensionname)
            print ("dimension id:", dimensionuuid)
            print ("Grabbing the mitigation rules JSON")
            url = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/positions?attribures=match,enabled&api_key=' + API_Key
            #print ("\nDEBUG: url: " , url)
            positionlist = requests.get(url, verify=False).json()
            #print ("\nDEBUG: positionlist: " , positionlist)
            json_formatted_positionlist = json.dumps(positionlist, indent=2)
            #print ("\nDEBUG: json_formatted_positionlist: " , json_formatted_positionlist)
            #for each position id in the selected dimension dump the details
            print ("This will be a big list, so I will also write it to file mitigation_rules.txt")
            print ("An example api query for one mitigation rules position looks like this.")
            print ("Where x is each positions id in the dimension")
            print ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "/position/x?attribures=match,enabled&api_key=" + API_Key + "' | json_pp")
            print ("I'll extract the list of rules and dump each one for you")
            input("Press any key to continue...")
            with open('mitigation_rules.txt', 'w') as f:
                for key in positionlist:
                    #print ("\nDEBUG: key: " , key)
                    url2 = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/position/' + str(key) + '?attribures=match,enabled&api_key=' + API_Key
                    positiondetails = requests.get(url2, verify=False).json()
                    json_formatted_positiondetails = json.dumps(positiondetails, indent=2)
                    print (json_formatted_positiondetails)
                    f.write(str(json_formatted_positiondetails))
            print ("Output was also write it to file mitigation_rules.txt")
        elif(ch == 10):
            print("Dump the countermeasure dimension positions in JSON")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            #find the countermeasure dimension uuid
            index = 0
            for key in dimensionlist:
                #print ("DEBUG: dimensionname ", dimensionlist[key]['name'])
                if dimensionlist[key]['name'] == "countermeasure":
                    dimensionuuid = dimensionlist[key]['dimension_id']
                    dimensionname = dimensionlist[key]['name']
            print ("dimension name:", dimensionname)
            print ("dimension id:", dimensionuuid)
            print ("Grabbing the countermeasure positions in  JSON")
            url = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/positions?attribures=match,enabled&api_key=' + API_Key
            #print ("\nDEBUG: url: " , url)
            positionlist = requests.get(url, verify=False).json()
            #print ("\nDEBUG: positionlist: " , positionlist)
            json_formatted_positionlist = json.dumps(positionlist, indent=2)
            #print ("\nDEBUG: json_formatted_positionlist: " , json_formatted_positionlist)
            #for each position id in the selected dimension dump the details
            print ("This will be a big list, so I will also write it to file countermeasures.txt")
            print ("An example api query for one countermeasures position looks like this.")
            print ("Where x is each positions id in the dimension")
            print ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "/position/x?attribures=match,enabled&api_key=" + API_Key + "' | json_pp")
            print ("I'll extract the list of countermeasures and dump each one for you")
            input("Press any key to continue...")
            with open('countermeasures.txt', 'w') as f:
                for key in positionlist:
                    #print ("\nDEBUG: key: " , key)
                    url2 = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/position/' + str(key) + '?attribures=match,enabled&api_key=' + API_Key
                    positiondetails = requests.get(url2, verify=False).json()
                    json_formatted_positiondetails = json.dumps(positiondetails, indent=2)
                    print (json_formatted_positiondetails)
                    f.write(str(json_formatted_positiondetails))
            print ("Output was also write it to file countermeasures.txt")
        elif(ch == 11):
            print("Flip all policies to use flow rather than spm (config-sync use case)")
            url = 'https://' + cluster_fqdn + '/api/defender/policies?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            policylist = requests.get(url, verify=False).json()
            #print ("\nDebug policylist: " , policylist)
            json_formatted_policylist = json.dumps(policylist, indent=2)
            #print ("\nDebug policylist: " , json_formatted_policylist)
            #for each policy is_spm == false 
            user_input = input("Input yes and I will  disable spm on all defender policies:")
            if user_input == 'yes':
                for key in policylist:
                     #print ("\nDEBUG: key: " , key)
                     if key == "entities":
                        #print ("\nDEBUG: policylist when id=entities: " , policylist[key])
                        for entities in policylist[key]:
                             policyentitlesid = entities['id']
                             #print ("\nDEBUG:policyentitlesid: " , policyentitlesid)
                             mycmd = ("curl -k --silent -X PATCH -H 'Content-Type: application/json' -d '{\"id\": " + str(policyentitlesid) + ", \"is_spm\": false}' 'https://" + cluster_fqdn + "/api/defender/policy/" + str(policyentitlesid) + "?api_key=" + API_Key + "' | json_pp > policies-entities.json")
                             #print("\nDEBUG: mycmd: " , mycmd )
                             os.system(mycmd)
                print("All Done")
                print("Changes have been written to file policies-entities.json")
        elif(ch == 12):
            print("Flip all policies to use spm rather than flow (config-sync use case)")
            url = 'https://' + cluster_fqdn + '/api/defender/policies?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            policylist = requests.get(url, verify=False).json()
            #print ("\nDebug policylist: " , policylist)
            json_formatted_policylist = json.dumps(policylist, indent=2)
            #print ("\nDebug policylist: " , json_formatted_policylist)
            #for each policy is_spm == false 
            user_input = input("Input yes and I will enable spm on all defender policies:")
            if user_input == 'yes':
                for key in policylist:
                     #print ("\nDEBUG: key: " , key)
                     if key == "entities":
                        #print ("\nDEBUG: policylist when id=entities: " , policylist[key])
                        for entities in policylist[key]:
                             policyentitlesid = entities['id']
                             #print ("\nDEBUG:policyentitlesid: " , policyentitlesid)
                             mycmd = ("curl -k --silent -X PATCH -H 'Content-Type: application/json' -d '{\"id\": " + str(policyentitlesid) + ", \"is_spm\": true}' 'https://" + cluster_fqdn + "/api/defender/policy/" + str(policyentitlesid) + "?api_key=" + API_Key + "' | json_pp > policies-entities.json")
                             #print("\nDEBUG: mycmd: " , mycmd )
                             os.system(mycmd)
                print("All Done")
                print("Changes have been written to file policies-entities.json")

#here
        elif(ch == 13):
            print ("Dumping all mitigation devices via the api")
            mycmd = ("curl --insecure -X GET https://" + cluster_fqdn + "/api/defender/mitigation/devices?api_key=" + API_Key + " | json_pp | tee mitigation-devices.json" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
            print ("The json has also been written to file ./mitigation-devices.json")
        elif(ch == 14):
            print ("Dumping all mitigation device groups via the api")
            mycmd = ("curl --insecure -X GET https://" + cluster_fqdn + "/api/defender/mitigation/groups?api_key=" + API_Key + " | json_pp | tee mitigation-device-groups.json" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
            print ("The json has also been written to file ./mitigation-device-groups.json")
        elif ch == 15:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu22
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tCollect the logs and slice.json on all DCUs")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    print ("Cleaning up old log backups")
    mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/log.*.tar.gz || true\"")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("tar and zip up the log files on all DCUs")
    mycmd = ("sudo salt -t 3600 \* cmd.run 'tar czvf /pipedream/tmp/log.`hostname`.tar.gz /var/log/ /pipedream/log/ /pipedream/cache/config/slice.json || true'")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("Setting file permissions")
    mycmd = ("sudo salt \* cmd.run 'chown support:support /pipedream/tmp/log.`hostname`.tar.gz'")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("Copying the files from the workers back to master")
    mycmd = ("for i in $(awk '{if(/mgmt/ && /worker/){print $1}}' /etc/hosts); do scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q $i:/pipedream/tmp/log.worker*.tar.gz /pipedream/tmp; done")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("tar up the tar files")
    mycmd = ("tar cvf /pipedream/tmp/defender-all-logs.tar.gz /pipedream/tmp/log*.tar.gz")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print ("Clean up")
    mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/log.*.tar.gz || true\"")
    print("Command is:" + mycmd )
    #input("Press any key and I'll run the command...")
    os.system(mycmd)
    print("\n\nThe resultant file /pipedream/tmp/defender-all-logs.tar.gz is going to be large (10-20G in size).") 
    print("move the file to your laptop, example laptop command follows") 
    print("scp [host]/pipedream/tmp/defender-all-logs.tar.gz .") 
    print("then use the next menu option to clean up") 
    input("Press enter to return to the previouse menu")
    os.system("clear")
    topmenu() 


def submenu220():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDimensions")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Dump the json for a dimension, selected from a list of all Dimensions
            2.Add a Dimension from a json file
            3.Create a protected object (custom data view) with subnets covering the internet. Step by step example
            4.Delete a dimension, selected from a list of all provisioned dimensions
            5.Dump the csv for all positions in a dimension, the dimension is selected from a list of all Dimensions
            6.Dump the JSON for all positions in a dimension, selected from a list of all dimensions
            7.Delete all positions in a dimension, selected from a list of all dimensions
            8.Set all positions in a dimension to disabled, selected from a list of all dimensions
            9.Set all positions in a dimension to enabled, selected from a list of all dimensions
            10.Delete one position in a dimension, selected from menu lists 
            11.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            print("Dump a specific dimension, selected from a menu of all configured dimensions")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            user_input = ''
            input_message = "Select a dimension:\n"
            index = 0
            for key in dimensionlist:
                index += 1
                #print ("DEBUG: key:", key)
                dimensionname = dimensionlist[key]['name']
                dimensionuuid = dimensionlist[key]['dimension_id']
                #dimensionname = key['name']
                #dimensionuuid = key['dimension_id']
                input_message += f'{index}) {dimensionname}\n'
            input_message += 'You selected dimension: '
            #prompt for the dimension by number x) 
            user_input = input(input_message)
            #now find the selected dimension name and uuid for the selected number
            index = 0
            for key in dimensionlist:
                index += 1
                if index == int(user_input):
                    dimensionname = dimensionlist[key]['name']
                    dimensionuuid = dimensionlist[key]['dimension_id']
            print ("You selected dimension name:", dimensionname)
            print ("Which has dimension id:", dimensionuuid)
            print ("Grabbing the dimension details for you")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "?api_key=" + API_Key + "' | json_pp | tee mydimension.json") 
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("\n\nI've written the output to file mydimension.json for you")
        elif(ch == 2):
            print("Create a new dimension from a json file - A step by step")
            dimension_filename = input("enter the json filename to import the dimension from:")
            DimensionName=input("Enter a name for your new custom dimension: ")
            print("\n\nThe following command will add the JSON in order to create a new data view")
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@" + dimension_filename + "' https://" + cluster_fqdn + "/dimension/" + DimensionName + "?api_key=" + API_Key)
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will create the dimension for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing. You can use the curl above to create the dimension yourself")
        elif(ch == 3):
            print("Create an example protected object (custom dimension) with a couple of subnets - A step by step")
            CustomDimension = """{
   "metadata" : {
      "attributes" : {
         "split" : true
      },
      "description" : "Test Protection Object",
      "split" : true
   }
}
"""
            print ("\n\nPrinting the custom dimension example\n", CustomDimension)
            print ("\n\nWriting the JSON ddos example to file custom-dimension-example.json\n\n")
            with open('custom-dimension-example.json', 'w') as f:
               f.write(str(CustomDimension))  
            DimensionName="ExampleCustomProtectedObject"
            print ("\n\nI will create the example custom dimension / protected object with name ", DimensionName)
            print ("\nThe following command will create the new custom dimension")
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@custom-dimension-example.json' https://" + cluster_fqdn + "/dimension/" + DimensionName + "?api_key=" + API_Key)
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will create the dimension for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
                ###########
                print("Now lets add the positions containing the subnets\n")
                input("Press enter to continue")
                SubnetList = """match:cidrs,position_id,display_name,description,name
7.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
11.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
12.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
4.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
1.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
5.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
13.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
14.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
9.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
6.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
0.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
3.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
10.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
8.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
2.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
15.0.0.0/8,1,0.0.0.0/4,0.0.0.0/4,0.0.0.0/4
19.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
27.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
22.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
18.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
16.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
23.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
25.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
30.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
26.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
24.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
31.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
17.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
28.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
20.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
21.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
29.0.0.0/8,2,16.0.0.0/4,16.0.0.0/4,16.0.0.0/4
44.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
33.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
46.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
39.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
35.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
32.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
36.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
47.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
41.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
34.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
43.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
40.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
38.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
45.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
37.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
42.0.0.0/8,3,32.0.0.0/4,32.0.0.0/4,32.0.0.0/4
63.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
54.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
55.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
50.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
51.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
59.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
60.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
62.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
48.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
52.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
61.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
58.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
56.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
53.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
57.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
49.0.0.0/8,4,48.0.0.0/4,48.0.0.0/4,48.0.0.0/4
72.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
67.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
68.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
70.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
76.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
66.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
74.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
69.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
64.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
71.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
77.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
78.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
73.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
79.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
75.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
65.0.0.0/8,5,64.0.0.0/4,64.0.0.0/4,64.0.0.0/4
94.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
87.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
80.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
85.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
91.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
95.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
90.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
84.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
88.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
86.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
92.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
81.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
89.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
93.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
82.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
83.0.0.0/8,6,80.0.0.0/4,80.0.0.0/4,80.0.0.0/4
101.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
102.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
109.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
97.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
106.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
96.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
98.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
105.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
103.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
107.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
100.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
111.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
104.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
108.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
110.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
99.0.0.0/8,7,96.0.0.0/4,96.0.0.0/4,96.0.0.0/4
112.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
120.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
119.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
125.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
126.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
114.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
122.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
117.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
118.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
121.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
127.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
116.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
123.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
113.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
124.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
115.0.0.0/8,8,112.0.0.0/4,112.0.0.0/4,112.0.0.0/4
140.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
129.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
137.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
135.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
138.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
128.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
130.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
142.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
143.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
139.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
136.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
141.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
134.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
133.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
132.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
131.0.0.0/8,9,128.0.0.0/4,128.0.0.0/4,128.0.0.0/4
146.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
145.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
150.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
147.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
156.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
159.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
144.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
151.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
153.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
148.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
155.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
149.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
152.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
158.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
154.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
157.0.0.0/8,10,144.0.0.0/4,144.0.0.0/4,144.0.0.0/4
170.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
165.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
161.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
163.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
168.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
160.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
167.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
164.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
166.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
172.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
174.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
175.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
173.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
169.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
171.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
162.0.0.0/8,11,160.0.0.0/4,160.0.0.0/4,160.0.0.0/4
183.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
186.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
177.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
178.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
179.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
182.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
181.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
176.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
188.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
187.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
189.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
190.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
180.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
185.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
184.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
191.0.0.0/8,12,176.0.0.0/4,176.0.0.0/4,176.0.0.0/4
207.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
201.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
194.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
196.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
198.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
203.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
192.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
204.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
197.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
202.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
205.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
199.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
195.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
206.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
200.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
193.0.0.0/8,13,192.0.0.0/4,192.0.0.0/4,192.0.0.0/4
212.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
208.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
214.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
220.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
213.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
211.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
215.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
217.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
218.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
222.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
223.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
210.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
219.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
221.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
216.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
209.0.0.0/8,14,208.0.0.0/4,208.0.0.0/4,208.0.0.0/4
232.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
239.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
225.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
224.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
233.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
235.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
226.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
237.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
238.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
227.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
229.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
228.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
234.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
236.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
231.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
230.0.0.0/8,15,224.0.0.0/4,224.0.0.0/4,224.0.0.0/4
241.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
252.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
248.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
255.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
245.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
246.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
251.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
249.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
243.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
250.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
240.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
244.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
247.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
253.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
254.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
242.0.0.0/8,16,240.0.0.0/4,240.0.0.0/4,240.0.0.0/4
"""
                print ("\n\nI've writted a list of subnets covering all IPV4 addresses to file subnet-example.csv\n\n")
                with open('subnet-example.csv', 'w') as f:
                   f.write(str(SubnetList))  
                print ("\n\nWe will use the Deepscript endpoint to read our csv file and turn it into positions.")
                print ("\nThe following command will create the positions in our custom dimension")
                mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' --data-binary '@subnet-example.csv' https://" + cluster_fqdn + "/deepscript/dimension/" + DimensionName + "?api_key=" + API_Key)
                print("Command is:" + mycmd )
                user_input = input("Input yes and I will create the positions for you, any other key to do nothing at all:")
                if user_input == 'yes':
                    print("\nRunning Command: " + mycmd )
                    os.system(mycmd)
                    print("\nDone")
        elif(ch == 4):
            print("Delete a specific dimension, selected from a menu of all configured dimensions")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            user_input = ''
            input_message = "Select a dimension:\n"
            index = 0
            for key in dimensionlist:
                index += 1
                #print ("DEBUG: key:", key)
                dimensionname = dimensionlist[key]['name']
                dimensionuuid = dimensionlist[key]['dimension_id']
                #dimensionname = key['name']
                #dimensionuuid = key['dimension_id']
                input_message += f'{index}) {dimensionname}\n'
            input_message += 'You selected dimension: '
            #prompt for the dimension by number x) 
            user_input = input(input_message)
            #now find the selected dimension name and uuid for the selected number
            index = 0
            for key in dimensionlist:
                index += 1
                if index == int(user_input):
                    dimensionname = dimensionlist[key]['name']
                    dimensionuuid = dimensionlist[key]['dimension_id']
            print ("You selected dimension name:", dimensionname)
            print ("Which has dimension id:", dimensionuuid)
            mycmd = ("curl -k --silent -X DELETE 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "?api_key=" + API_Key + "' | json_pp ") 
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will delete the dimension for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\n\nAll Done")
        elif(ch == 5):
            print("Dump the csv for all positions in a dimension, the dimension is selected from a list of all Dimensions")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            user_input = ''
            input_message = "Select a dimension:\n"
            index = 0
            for key in dimensionlist:
                index += 1
                #print ("DEBUG: key:", key)
                dimensionname = dimensionlist[key]['name']
                dimensionuuid = dimensionlist[key]['dimension_id']
                #dimensionname = key['name']
                #dimensionuuid = key['dimension_id']
                input_message += f'{index}) {dimensionname}\n'
            input_message += 'You selected dimension: '
            #prompt for the dimension by number x) 
            user_input = input(input_message)
            #now find the selected dimension name and uuid for the selected number
            index = 0
            for key in dimensionlist:
                index += 1
                if index == int(user_input):
                    dimensionname = dimensionlist[key]['name']
                    dimensionuuid = dimensionlist[key]['dimension_id']
            print ("You selected dimension name:", dimensionname)
            print ("Which has dimension id:", dimensionuuid)
            print ("Grabbing the dimension positions for you")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "/positions/download?filetype=csv&api_key=" + API_Key + "' | tee example-dimension-position.csv") 
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command to output the csv...")
            os.system(mycmd)
            print("\nI've also written the csv to a file for you example-dimension-position.csv...")
        elif(ch == 6):
            print("Dump the JSON for all positions in a dimension, selected from a list of all dimensions")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            user_input = ''
            input_message = "Select a dimension:\n"
            index = 0
            for key in dimensionlist:
                index += 1
                #print ("DEBUG: key:", key)
                dimensionname = dimensionlist[key]['name']
                dimensionuuid = dimensionlist[key]['dimension_id']
                #dimensionname = key['name']
                #dimensionuuid = key['dimension_id']
                input_message += f'{index}) {dimensionname}\n'
            input_message += 'You selected dimension: '
            #prompt for the dimension by number x) 
            user_input = input(input_message)
            #now find the selected dimension name and uuid for the selected number
            index = 0
            for key in dimensionlist:
                index += 1
                if index == int(user_input):
                    dimensionname = dimensionlist[key]['name']
                    dimensionuuid = dimensionlist[key]['dimension_id']
            print ("You selected dimension name:", dimensionname)
            print ("Which has dimension id:", dimensionuuid)
            print ("Grabbing the dimension position ids and printing the details")
            url = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/positions?attribures=match,enabled&api_key=' + API_Key
            #print ("\nDEBUG: url: " , url)
            positionlist = requests.get(url, verify=False).json()
            #print ("\nDEBUG: positionlist: " , positionlist)
            json_formatted_positionlist = json.dumps(positionlist, indent=2)
            #print ("\nDEBUG: json_formatted_positionlist: " , json_formatted_positionlist)
            #for each position id in the selected dimension dump the details 
            print ("This will be a big list, so I will also write it to file dimension_positions.json")
            input("Press any key to continue...")
            with open('dimension_positions.json', 'w') as f:
                for key in positionlist:
                    #print ("\nDEBUG: key: " , key)
                    url2 = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/position/' + str(key) + '?attribures=match,enabled&api_key=' + API_Key
                    positiondetails = requests.get(url2, verify=False).json()
                    json_formatted_positiondetails = json.dumps(positiondetails, indent=2)
                    print (json_formatted_positiondetails)
                    f.write(str(json_formatted_positiondetails))
            print ("Output was also writen to file dimension_positions.json")
        elif(ch == 7):
            print("Delete all positions in a dimension, selected from a list of all dimensions")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            user_input = ''
            input_message = "Select a dimension:\n"
            index = 0
            for key in dimensionlist:
                index += 1
                #print ("DEBUG: key:", key)
                dimensionname = dimensionlist[key]['name']
                dimensionuuid = dimensionlist[key]['dimension_id']
                #dimensionname = key['name']
                #dimensionuuid = key['dimension_id']
                input_message += f'{index}) {dimensionname}\n'
            input_message += 'You selected dimension: '
            #prompt for the dimension by number x) 
            user_input = input(input_message)
            #now find the selected dimension name and uuid for the selected number
            index = 0
            for key in dimensionlist:
                index += 1
                if index == int(user_input):
                    dimensionname = dimensionlist[key]['name']
                    dimensionuuid = dimensionlist[key]['dimension_id']
            print ("You selected dimension name:", dimensionname)
            print ("Which has dimension id:", dimensionuuid)
            url = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/positions?attribures=match,enabled&api_key=' + API_Key
            #print ("\nDEBUG: url: " , url)
            positionlist = requests.get(url, verify=False).json()
            #print ("\nDEBUG: positionlist: " , positionlist)
            json_formatted_positionlist = json.dumps(positionlist, indent=2)
            #print ("\nDEBUG: json_formatted_positionlist: " , json_formatted_positionlist)
            #for each position id in the selected dimension dump the details 
            positionlistseperated = "[" 
            for key in positionlist:
                #print ("\nDEBUG: key: " , key)
                #url2 = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/position/' + str(key) + '?attribures=match,enabled&api_key=' + API_Key
                #positiondetails = requests.get(url2, verify=False).json()
                positionlistseperated = positionlistseperated + key + "," 
                print ("\nDEBUG: positionlistseperated: " , positionlistseperated)
            positionlistseperated = positionlistseperated.rstrip(',')
            positionlistseperated = positionlistseperated + "]" 
            print ("\nDEBUG: positionlistseperated: " , positionlistseperated)
            #curl -X DELETE -d '{"data": {"positions": [2,4]}}' "https://{host}/dimension/10001/positions?api_key={api-key}"
            mycmd = ("curl -k --silent -X DELETE -d '{\"data\": {\"positions\": " + positionlistseperated + "}}' 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "/positions" + "?api_key=" + API_Key + "' | json_pp ")
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will delete the dimension positions for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\n\nAll Done")
        elif(ch == 8):
            print("set all positions in a dimension to disabled, selected from a list of all dimensions")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            user_input = ''
            input_message = "Select a dimension:\n"
            index = 0
            for key in dimensionlist:
                index += 1
                #print ("DEBUG: key:", key)
                dimensionname = dimensionlist[key]['name']
                dimensionuuid = dimensionlist[key]['dimension_id']
                #dimensionname = key['name']
                #dimensionuuid = key['dimension_id']
                input_message += f'{index}) {dimensionname}\n'
            input_message += 'You selected dimension: '
            #prompt for the dimension by number x) 
            user_input = input(input_message)
            #now find the selected dimension name and uuid for the selected number
            index = 0
            for key in dimensionlist:
                index += 1
                if index == int(user_input):
                    dimensionname = dimensionlist[key]['name']
                    dimensionuuid = dimensionlist[key]['dimension_id']
            print ("You selected dimension name:", dimensionname)
            print ("Which has dimension id:", dimensionuuid)
            url = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/positions?attribures=match,enabled&api_key=' + API_Key
            #print ("\nDEBUG: url: " , url)
            positionlist = requests.get(url, verify=False).json()
            #print ("\nDEBUG: positionlist: " , positionlist)
            json_formatted_positionlist = json.dumps(positionlist, indent=2)
            #print ("\nDEBUG: json_formatted_positionlist: " , json_formatted_positionlist)
            #for each position id in the selected dimension disable the position 
            user_input = input("Input yes and I will disable the dimension positions for you, any other key to do nothing at all:")
            if user_input == 'yes':
                for key in positionlist:
                    #print ("\nDEBUG: key: " , key)
                    mycmd = ("curl -k --silent -X PUT -H 'Content-Type: application/json' -d '{\"enabled\":\"false\"}' 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "/position/" + key + "?api_key=" + API_Key + "' | json_pp ")
                    print("\nRunning Command: " + mycmd )
                    os.system(mycmd)
                print("\n\nAll Done")
        elif(ch == 9):
            print("set all positions in a dimension to enabled, selected from a list of all dimensions")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            user_input = ''
            input_message = "Select a dimension:\n"
            index = 0
            for key in dimensionlist:
                index += 1
                #print ("DEBUG: key:", key)
                dimensionname = dimensionlist[key]['name']
                dimensionuuid = dimensionlist[key]['dimension_id']
                #dimensionname = key['name']
                #dimensionuuid = key['dimension_id']
                input_message += f'{index}) {dimensionname}\n'
            input_message += 'You selected dimension: '
            #prompt for the dimension by number x) 
            user_input = input(input_message)
            #now find the selected dimension name and uuid for the selected number
            index = 0
            for key in dimensionlist:
                index += 1
                if index == int(user_input):
                    dimensionname = dimensionlist[key]['name']
                    dimensionuuid = dimensionlist[key]['dimension_id']
            print ("You selected dimension name:", dimensionname)
            print ("Which has dimension id:", dimensionuuid)
            url = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/positions?attribures=match,enabled&api_key=' + API_Key
            #print ("\nDEBUG: url: " , url)
            positionlist = requests.get(url, verify=False).json()
            #print ("\nDEBUG: positionlist: " , positionlist)
            json_formatted_positionlist = json.dumps(positionlist, indent=2)
            #print ("\nDEBUG: json_formatted_positionlist: " , json_formatted_positionlist)
            #for each position id in the selected dimension disable the position 
            user_input = input("Input yes and I will enable the dimension positions for you, any other key to do nothing at all:")
            if user_input == 'yes':
                for key in positionlist:
                    #print ("\nDEBUG: key: " , key)
                    mycmd = ("curl -k --silent -X PUT -H 'Content-Type: application/json' -d '{\"enabled\":\"true\"}' 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "/position/" + key + "?api_key=" + API_Key + "' | json_pp ")
                    print("\nRunning Command: " + mycmd )
                    os.system(mycmd)
                print("\n\nAll Done")
        elif(ch == 10):
            print("Delete one position in a dimension, selected from menu lists")
            url = 'https://' + cluster_fqdn + '/dimensions/index?attributes=*&api_key=' + API_Key
            #print ("\nDebug url: " , url)
            dimensionlist = requests.get(url, verify=False).json()
            #print ("\nDimensionlist: " , dimensionlist)
            json_formatted_dimensionlist = json.dumps(dimensionlist, indent=2)
            #print ("\nDebug dimensionlist: " , json_formatted_dimensionlist)
            #build the text menu
            user_input = ''
            input_message = "Select a dimension:\n"
            index = 0
            for key in dimensionlist:
                index += 1
                #print ("DEBUG: key:", key)
                dimensionname = dimensionlist[key]['name']
                dimensionuuid = dimensionlist[key]['dimension_id']
                #dimensionname = key['name']
                #dimensionuuid = key['dimension_id']
                input_message += f'{index}) {dimensionname}\n'
            input_message += 'You selected dimension: '
            #prompt for the dimension by number x) 
            user_input = input(input_message)
            #now find the selected dimension name and uuid for the selected number
            index = 0
            for key in dimensionlist:
                index += 1
                if index == int(user_input):
                    dimensionname = dimensionlist[key]['name']
                    dimensionuuid = dimensionlist[key]['dimension_id']
            print ("You selected dimension name:", dimensionname)
            print ("Which has dimension id:", dimensionuuid)
            #build the possitions text menu
            #for the selected dimension
            url = 'https://' + cluster_fqdn + '/dimension/' + str(dimensionuuid) + '/positions?attributes=*&api_key=' + API_Key
            #print ("\nDebug possitions url: " , url)
            possitionlist = requests.get(url, verify=False).json()
            #print ("\nDebug possitionlist: " , possitionlist)
            json_formatted_possitionlist = json.dumps(possitionlist, indent=2)
            #print ("\nDebug json formatted possitionlist: " , json_formatted_possitionlist)
            user_input = ''
            input_message = "Select a possition to delete from this list of possition names and id's:\n"
            index = 0
            for key in possitionlist:
                index += 1
                #print ("DEBUG: key:", key)
                possitionname = possitionlist[key]['name']
                possitionuuid = possitionlist[key]['id']
                input_message += f'{index}) name={possitionname} id={possitionuuid}\n'
            input_message += 'You selected possition: '
            #prompt for the possition by number x) 
            user_input = input(input_message)
            #now find the selected possition name and uuid for the selected number
            index = 0
            for key in possitionlist:
                index += 1
                if index == int(user_input):
                    possitionname = possitionlist[key]['name']
                    possitionuuid = possitionlist[key]['id']
            print ("You selected possition name:", possitionname)
            print ("Which has possition id:", possitionuuid)
            positionlist = requests.get(url, verify=False).json()
            #print ("\nDEBUG: positionlist: " , positionlist)
            json_formatted_positionlist = json.dumps(positionlist, indent=2)
            #print ("\nDEBUG: json_formatted_positionlist: " , json_formatted_positionlist)
            #prompt then if the user enters yea delete the possition
            mycmd = ("curl -k --silent -X DELETE -d '{\"data\": {\"positions\": [" + str(possitionuuid) + "]}}' 'https://" + cluster_fqdn + "/dimension/" + str(dimensionuuid) + "/positions" + "?api_key=" + API_Key + "' | json_pp ")
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will delete the dimension positions for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\n\nAll Done")
        elif ch == 11:
            topmenu()
        else:
            print("Invalid entry")
        input("\nPress enter to continue")
        os.system("clear")
        submenu220()
def submenu221():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tOrganizations and Users")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Dump a list of all organization user id's mapped to email address 
            2.Dump a formatted json list of all users configuration
            3.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            print("Dump a list of all organization user id's mapped to email address")
            url = 'https://' + cluster_fqdn + '/api/users?attributes=*&api_key=' + API_Key
            #print ("\nDEBUG: url: " , url)
            userlist = requests.get(url, verify=False).json()
            #print ("\nDEBUG: userlist: " , userlist)
            json_formatted_userlist = json.dumps(userlist, indent=2)
            #print ("\nDEBUG: json formatted userlist: " , json_formatted_userlist)
            index = 0
            for key in userlist['users']:
                #print ("DEBUG: userlist key ", key)
                userid = userlist['users'][key]['id'] 
                #print ("DEBUG: userid ", userid)
                useremail = userlist['users'][key]['email']
                #print ("DEBUG: email:", useremail)
                print(" user id: " + userid + " email: " + useremail )
        elif(ch == 2):
            print("Dump a formatted json list of all users configuration")
            mycmd = ("curl --insecure -X GET 'https://" + cluster_fqdn + "/api/users/?&attributes=(*)&api_key=" + API_Key + "' | json_pp | tee userlist.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("\n\nI've written the output to file userlist.json for you")
        elif ch == 3:
            topmenu()
        else:
            print("Invalid entry")
        input("\nPress enter to continue")
        os.system("clear")
        submenu221()

def submenu222():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tBoundaries")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Dump a formatted json list of all Boundaries 
            2.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            print("Dump a formatted json list of all users configuration")
            mycmd = ("curl --insecure -X GET 'https://" + cluster_fqdn + "/api/boundaries?api_key=" + API_Key + "' | json_pp | tee boundaries.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("\n\nI've written the output to file boundaries.json for you")
        elif ch == 2:
            topmenu()
        else:
            print("Invalid entry")
        input("\nPress enter to continue")
        os.system("clear")
        submenu221()

def submenu212():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Networking (must be ran on the master)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.show the interfaces on each node 
            2.show the routes on each node 
            3.show if the bond is up on each node 
            4.show the full bond status on each node 
            5.show interface drops on each node 
            6.show per protocol interface statistics on each node (long one) 
            7.show all listening ports on all nodes (long one) 
            8.show who is attached to a port you specify, on all nodes 
            9.show ntp status on all nodes 
            10.show the date and time on all nodes 
            11.test connectivity to Deepfield genome
            12.test connectivity to Deepfield metrics 
            13.test connectivity to Deepfield downloads 
            14.dump /etc/network/interfaces for all nodes
            15.dump all DCU's network configuration to all DCU's file /home/support/network-all-files-all-hosts.tar.gz, Use before a reboot.
            16.Audit the DCUs network configuration, static and dynamic
            17.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycmd = "sudo salt \* cmd.run \"ip addr show\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 2):
            mycmd = "sudo salt \* cmd.run \"netstat -rn\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 3):
            mycmd = "sudo salt \* cmd.run \"cat /proc/net/bonding/bond0 | grep up\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 4):
            mycmd = "sudo salt \* cmd.run \"cat /proc/net/bonding/bond0\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 5):
            mycmd = "sudo salt \* cmd.run \"netstat -i\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 6):
            mycmd = "sudo salt \* cmd.run \"netstat -s\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 7):
            mycmd = "sudo salt \* cmd.run \"sudo netstat -tulpn | grep LISTEN\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 8):
            myport=input("Enter your port: ")
            mycmd = "sudo salt \* cmd.run \"sudo lsof -i:" + myport + "\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 9):
            mycmd = "sudo salt \* cmd.run \"ntpq -p\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 10):
            mycmd = "sudo salt \* cmd.run \"date\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 11):
            mycmd = "sudo salt \* cmd.run \"nc -zv genome.deepfield.net 443\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 12):
            mycmd = "sudo salt \* cmd.run \"nc -zv monitoring.deepfield.net 443\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 13):
            mycmd = "sudo salt \* cmd.run \"nc -zv download.deepfield.net 443\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 14):
            mycmd = "sudo salt \* cmd.run \"cat /etc/network/interfaces\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 15):
            print("\t-------------------------------------------------")
            print ("Step 1)Cleaning up old tar files")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/network-config* || true\"")
            mycmd = ("sudo rm -f /pipedream/tmp/network-all-files-all-hosts.tar.gz")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 2)tar'ing and zip'ing up the network config files on all DCUs,")
            print("\t-------------------------------------------------")
            mycmd = "sudo salt \* cmd.run \"echo ****ip-addr-show*** > /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"ip addr show | tee -a /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"echo ****ifconfig*** >> /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"ifconfig | tee -a /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"echo ****netstat-rn*** >> /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = "sudo salt \* cmd.run \"netstat -rn | tee -a /pipedream/tmp/network-config-dynamic-config.`hostname`.txt\""
            os.system(mycmd)
            mycmd = ("sudo salt -t 3600 \* cmd.run 'tar czvf /pipedream/tmp/network-config.`hostname`.tar.gz /etc/network/interfaces /etc/network/interfaces.d /etc/resolv.conf /etc/hosts /pipedream/tmp/network-config-dynamic-config* || true'")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step3) Setting file permissions")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt \* cmd.run 'chown support:support /pipedream/tmp/network-config.`hostname`.tar.gz'")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 4)Copying the files from the workers back to master")
            print("\t-------------------------------------------------")
            mycmd = ("for i in $(awk '{if(/mgmt/ && /worker/){print $1}}' /etc/hosts); do scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q $i:/pipedream/tmp/network-config.worker*.tar.gz /pipedream/tmp; done")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 5)tar'ing up the tar files into one big file")
            print("\t-------------------------------------------------")
            mycmd = ("tar cvf /pipedream/tmp/network-all-files-all-hosts.tar.gz /pipedream/tmp/network-config.*.tar.gz")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 6)Clean up")
            print("\t-------------------------------------------------")
            mycmd = ("sudo salt \* cmd.run \"rm -f /pipedream/tmp/network-config* || true\"")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t-------------------------------------------------")
            print ("Step 7)Copying the big zip file back out to all the workers")
            print("\t-------------------------------------------------")
            mycmd = ("for i in $(awk '{if(/mgmt/){print $1}}' /etc/hosts); do scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q /pipedream/tmp/network-all-files-all-hosts.tar.gz $i:/home/support/network-all-files-all-hosts.tar.gz; done")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("All Done") 
            print("\n\n=====================================================================================================") 
            print("The resultant file /home/support/network-all-files-all-hosts.tar.gz") 
            print("is on all DCU's and contains every DCU's dynamic and static network configuration") 
            print("=====================================================================================================") 
            input("Press enter to return to the menu")
            os.system("clear")
            submenu212()
        elif(ch == 16):
            print("\t-----------------------------------------------")
            print ("Copying network-audit.py out to all DCU's")
            print("\t-----------------------------------------------")
            mycmd = ("for i in $(awk '{if(/mgmt/){print $1}}' /etc/hosts); do scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q ./network-audit.py $i:/home/support/network-audit.py; done")
            os.system(mycmd)
            mycmd = ("sudo salt \* cmd.run \"chmod a+x /home/support/network-audit.py\"")
            os.system(mycmd)
            os.system("tput setaf 6")
            print("\t----------------------------------")
            print ("Runing netork-audit.py on all nodes")
            print("\t----------------------------------")
            mycmd = ("sudo salt \* cmd.run \"python3 /home/support/network-audit.py\"")
            os.system(mycmd)
            print("------------------------------")
            print ("----------All Done-----------")
            print ("-----------------------------")
        elif ch == 17:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu212()

def submenu214():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield MOPS and Backups (must be ran on the master)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.create a MOP directory on all DCUs based on todays date
            2.backup the network configuration static and dynamic into the MOP directory, on all DCUs
            3.backup the slice.json into the MOP directory, on all DCUs
            4.backup the soup status into the MOP directory, on Master for all DCUs
            5.delete todays mop directory, on all DCUs
            6.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycmd = ("sudo salt \* cmd.run \"mkdir -p /home/support/mop/mop-" + today + "\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 2):
            mycmd = ("sudo salt \* cmd.run \"cp /etc/network/interfaces /home/support/mop/mop-" + today + "/interfaces.bkup\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
            mycmd = ("sudo salt \* cmd.run \"ifconfig | tee /home/support/mop/mop-" + today + "/ifconfig.bkup\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
            mycmd = ("sudo salt \* cmd.run \"ip addr show | tee /home/support/mop/mop-" + today + "/ipaddr.bkup\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
            mycmd = ("sudo salt \* cmd.run \"netstat -rn | tee /home/support/mop/mop-" + today + "/netstat.bkup\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 3):
            mycmd = ("sudo salt \* cmd.run \"cp /pipedream/cache/config/slice.json /home/support/mop/mop-" + today + "/slice.json.bkup\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 4):
            mycmd = ("sudo salt \* cmd.run \"sudo supervisorctl status | tee /home/support/mop/mop-" + today + "/soup.status.bkup\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 5):
            mycmd = ("sudo salt \* cmd.run \"rm -rf /home/support/mop/mop-" + today + "\"")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 6):
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu214()

def submenu215():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tHDFS (must be ran on the master)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.HDFS Status Report
            2.List all HDFS Dimensions, sorted by size
            3.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycmd = ("hdfs dfsadmin -report")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 2):
            mycmd = ("hdfs dfs -ls /pipedream/cache/dimensions/ | sort -n -k+5")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 3):
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu215()


def submenu216():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDevices API")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Get the Device API Topology Schema
            2.Get the Device API utilisation Schema
            3.Get a list of routers via the devices API
            4.Get a list of routers using the routers dimension
            5.Get a list of all interfaces via the interface dimension (this is a big list, perhaps the next one is better)
            6.Get a list of interfaces for a given router via the interface dimension
            7.Build a router model from an existing router, so you can add/remove interfaces using the devices api 
            8.Set a single specified routers interface to 'active' true/false (psql so must be on master)
            9.count 'active' for all interfaces on a specified router (psql so must be on master)
            10.Set all interfaces on a specified router to 'active' true/false (receiving flow) (psql so must be on master)
            11.count 'active' for all interfaces on all routers (psql so must be on master)
            12.Set all interfaces 'active' true/false on all router (psql so must be on master)s
            13.Overwrite a specified routers interface name, intended for config rules (works but then gets reset to router name + ifname )
            14.Debugging hints
            15.Procedure to change any fields in an existing router using the dimensions api
            16.Procedure to create a new router/dms from an existing router/dms using the  dimension/router api
            17.Dump the udms mdms configs using /api/devices/dms 
            18.Delete a router selected from a list of all routers
            19.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            print("To see the Device API Topology Schema, point your browser here ")
            print("https://" + re.sub("^[a-z]+\.", "", socket.gethostname())+ "/docs/api/devices/topology")
        elif(ch == 2):
            print("To see the Device API Utilisation Schema, point your browser here ")
            print("https://" + re.sub("^[a-z]+\.", "", socket.gethostname())+ "/docs/api/devices/utilization")
        elif(ch == 3):
            print("Method GET is as of 5.4 not supported, so this command will fail. Only POST is supported")
            print("curl --insecure -X GET 'https:/" + cluster_fqdn + "/api/devices/topology?api_key=" + API_Key + "'")
            print("I've provided an alternative more complex methods in the following options")
        elif(ch == 4):
            print("Get a list of routers and attributes using the routers dimension")
            mycmd = ("curl --insecure -X GET 'https://" + cluster_fqdn + "/dimension/router/positions?&attributes=(*)&api_key=" + API_Key + "' | tee routerlist.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("\n\nI've written the output to file routerlist.json for you")
        elif(ch == 5):
            print("Get a list of all interfaces via the interface dimension")
            mycmd = ("curl --insecure -X GET 'https://" + cluster_fqdn + "/dimension/interfaces/positions?&attributes=(*)&api_key=" + API_Key + "' | tee interfacelist.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("\n\nI've written the output to file interfacelist.json for you")
        elif(ch == 6):
            print("Get a list of interfaces for a given router via the interface dimension")
            #url = 'https://' + cluster_fqdn + '/dimension/router/positions?api_key=' + API_Key
            url = 'https://' + cluster_fqdn + '/dimension/router/positions?attributes=*&api_key=' + API_Key
            routerlist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json
            json_formatted_routerlist = json.dumps(routerlist, indent=2)
            #print ("\nDebug routerlist: " , json_formatted_routerlist)
            #build the text menu
            user_input = ''
            input_message = "Select a router:\n"
            index = 0
            for key in routerlist:
                index += 1
                routername = routerlist[key]['name']
                input_message += f'{index}) {routername}\n'
            input_message += 'You selected router: '
            #prompt for the router by number x) 
            user_input = input(input_message)
            #now find the selected router name and position for the selected number
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerposition = routerlist[key]['position_id']
            print ("You selected Router name:", routername)
            print ("That Router has position:", routerposition)
            print ("The following command will get the router interfaces")
            mycmd = ("curl --insecure -X GET 'https://" + cluster_fqdn + "/dimension/interfaces/positions?filter=(interface:router_pos_id,=," + str(routerposition) + ")&attributes=(*)&api_key=" + API_Key + "' | tee myrouterinterfacelist.json")
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("\n\nI've written the output to file myrouterinterfacelist.json for you")
        elif(ch == 7):
            print("Build a router model from an existing router")
            print("show the POST to the Devices Topology API to recreate it") 
            print ("If you then add/delete interfaces to the topology.json file they will change in the router")
            print("This one works around the missing GET in devices API")
            print("I am Building up the router model from several places")
            #start by listing all routers and askign the user to pick one 
            url = 'https://' + cluster_fqdn + '/dimension/router/positions?attributes=*&api_key=' + API_Key
            routerlist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json containing all of the router info
            #json_formatted_routerlist = json.dumps(routerlist, indent=2)
            #print ("\nDebug routerlist: " , json_formatted_routerlist)
            #build the text menu
            user_input = ''
            input_message = "Select a router:\n"
            index = 0
            for key in routerlist:
                index += 1
                routername = routerlist[key]['name']
                input_message += f'{index}) {routername}\n'
            input_message += 'You selected router: '
            #prompt for the router by number x) 
            user_input = input(input_message)
            #
            #ok so we know the router. Lets gather up all of the information we need for the model 
            #
            #find the router name and the position
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerposition = routerlist[key]['position_id']
                    routerflowip = routerlist[key]['router']['flow_ip']
            #
            #get the router interfaces
            url = 'https://' + cluster_fqdn + '/dimension/interfaces/positions?filter=(interface:router_pos_id,=,' + str(routerposition) + ')&attributes=(*)&api_key=' + API_Key
            routerinterfaces = requests.get(url, verify=False).json()
            #for debug the line below prints the json containing all of the router interfaces
            #print ("\nDebug url: " + url)
            #json_formatted_routerinterfaces = json.dumps(routerinterfaces, indent=2)
            #print ("\nDebug routerinterfaces: ", json_formatted_routerinterfaces)
            #
            #we have router name, routername
            #we have the router position, routerposition
            #we have the router interfaces routerinterfaces json_formatted_routerinterfaces
            #we have the router flow ip routerflowip 
            #
            #so we have all of the details required for the model. lets build the json
            topologyjson = "{\n"
            topologyjson += f'  "devices": [\n'
            topologyjson += f'    {{\n'
            topologyjson += f'      "name": "{routername}",\n'
            topologyjson += f'      "flow_ip": "{routerflowip}",\n'
            topologyjson += f'      "interfaces": [\n'
            #we have to reformat the interfaces for the devices topology model
            #index = 0
            #for key in routerinterfaces["devices"]:
            #    print(routerinterfaces["devices"])
            for key in routerinterfaces:
                 index += 1
                 ifIndex = routerinterfaces[key]['interface']['ifIndex']
                 ifName = routerinterfaces[key]['interface']['ifName']
                 topologyjson += f'      {{\n'
                 topologyjson += f'          "ifIndex": {ifIndex},\n'
                 topologyjson += f'          "ifName": "{ifName}"\n'
                 topologyjson += f'      }},\n'
            #replace the last }, with a }
            topologyjson = (replace_last(topologyjson, '},', '}'))
            topologyjson += f'      ]\n'
            topologyjson += f'    }}\n'
            topologyjson += f'    ]\n'
            topologyjson += f'}}\n'

            #print ("Debug: topology_json\n", topologyjson)
            file = open("topologyConfigFile.json", "w")
            file.write(topologyjson)
            file.close
            #now show the command to provision the router model
            mycmd = ("curl --insecure -X POST -d '@topologyConfigFile.json' https://" + cluster_fqdn + "/api/devices/topology?api_key=" + API_Key)
            print("I have created a file for you topologyConfigFile.json with the routers topology model")
            print("Check the file over carefully")
            print("The device API POST is an update")
            print("The devices api does not add routers, so add the in the ui first")
            print("The devices api adds and updates interfaces")
            print("You can include all interfaces (with the risk that you change them) or just the new ones")
            print("for devices api to work snmp must be disabled 'unticked' on the router. Otherwise 200OK and nothing")
            print("for devices api to work the router must have a name and a description. Otherwise 200OK and nothing")
            print("I have not found a way to delete interfaces using device api")
            print("Interfaces come up with this missing in the interfaces dimension devices active: false the next option fixes that")
            print("Once you are happy copy paste the command below to provision/change the router or interface")
            print("\nCommand is:" + mycmd )
        elif(ch == 8):
            print ("Set a single routers interface to active true/false (receiving flow)")
            #first get a router from the list
            #start by listing all routers and askign the user to pick one 
            url = 'https://' + cluster_fqdn + '/dimension/router/positions?attributes=*&api_key=' + API_Key
            routerlist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json containing all of the router info
            #json_formatted_routerlist = json.dumps(routerlist, indent=2)
            #print ("\nDebug routerlist: " , json_formatted_routerlist)
            #build the text menu for the routers
            user_input = ''
            input_message = "Select a router:\n"
            index = 0
            for key in routerlist:
                index += 1
                routername = routerlist[key]['name']
                input_message += f'{index}) {routername}\n'
            input_message += 'You selected router: '
            #prompt for the router by number x) 
            user_input = input(input_message)
            #
            #find the router name and the position
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerposition = routerlist[key]['position_id']
                    routerflowip = routerlist[key]['router']['flow_ip']
            # now have the user select the router interface they want to enable/disable from a list
            url = 'https://' + cluster_fqdn + '/dimension/interfaces/positions?filter=(interface:router_pos_id,=,' + str(routerposition) + ')&attributes=(*)&api_key=' + API_Key
            routerinterfacelist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json containing all of the router info
            json_formatted_routerinterfacelist = json.dumps(routerinterfacelist, indent=2)
            #print ("\nDebug routerinterfacelist: " , json_formatted_routerinterfacelist)
            #build the text menu for the router interfaces
            user_input = ''
            input_message = "Select an interface from that router:\n"
            index = 0
            for key in routerinterfacelist:
                index += 1
                interfacename = routerinterfacelist[key]['name']
                input_message += f'{index}) {interfacename}\n'
            input_message += 'You selected router interface: '
            #prompt for the router interface by number x) 
            user_input = input(input_message)
            #find the interface position and name 
            index = 0
            for key in routerinterfacelist:
                index += 1
                if index == int(user_input):
                    #get the name of the selected interface
                    interfacenameselected = routerinterfacelist[key]['name']
                    #get the position of the selected interface
                    interfacepositionselected = routerinterfacelist[key]['id']
                    #get the json for the selected interface
                    routerinterfaceselectedjson = routerinterfacelist[key]
                    #print ("Debug: interfacenameselected=", interfacenameselected)
                    #print ("Debug: interfacepositionselected=", interfacepositionselected)
                    #print ("Debug: routerinterfaceselectedjson=", routerinterfaceselectedjson)
            print ("\nThe interfaces dimension api is buggy (5.4), doesn't allow us to set or add active")
            print ("So we are going to have to do this directly in postgress (5.4+)")
            print ("You selected router ", routername)
            print ("You selected interface ", interfacenameselected)
            print ("The interface can have three settings t/f/[blank]\nwhich means true false or no 'active' parameter present\nThe current setting for active is\n")
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active from \"Interfaces\" where id=" + str(interfacepositionselected) + " order by id;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )
            print("\nHow do you want me to set active)")
            user_input = input("Input true or false any other key makes no change:")
            if user_input == 'true':
                print ("setting to active=true. I used this comand")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'update \"Interfaces\" set active='true' where id=" + str(interfacepositionselected) + ";'")
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
        elif(ch == 9):
            print ("Count the 'active' settings t/f/[blank] on all interfaces of a specified router")
            #first get a router from the list
            #start by listing all routers and ask the user to pick one 
            url = 'https://' + cluster_fqdn + '/dimension/router/positions?attributes=*&api_key=' + API_Key
            routerlist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json containing all of the router info
            #json_formatted_routerlist = json.dumps(routerlist, indent=2)
            #print ("\nDebug routerlist: " , json_formatted_routerlist)
            #build the text menu for the routers
            user_input = ''
            input_message = "Select a router:\n"
            index = 0
            for key in routerlist:
                index += 1
                routername = routerlist[key]['name']
                input_message += f'{index}) {routername}\n'
            input_message += 'You selected router: '
            #prompt for the router by number x) 
            user_input = input(input_message)
            #
            #find the router name and the position
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerposition = routerlist[key]['position_id']
                    routerflowip = routerlist[key]['router']['flow_ip']
            # now have the user select the router interface they want to enable/disable from a list
            url = 'https://' + cluster_fqdn + '/dimension/interfaces/positions?filter=(interface:router_pos_id,=,' + str(routerposition) + ')&attributes=(*)&api_key=' + API_Key
            routerinterfacelist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json containing all of the router info
            json_formatted_routerinterfacelist = json.dumps(routerinterfacelist, indent=2)
            #print ("\nDebug routerinterfacelist: " , json_formatted_routerinterfacelist)

            #count the existing interfaces t/f/[blank]
            print ("Counting the t/f/[blank] interfaces for the router ", routername)
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active, COUNT(*) from \"Interfaces\" where _interface_router_pos_id=" + str(routerposition) + " group by active;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )

        elif(ch == 10):
            print ("Set all interfaces on a specified router to active true/false (receiving flow)")
            #first get a router from the list
            #start by listing all routers and ask the user to pick one 
            url = 'https://' + cluster_fqdn + '/dimension/router/positions?attributes=*&api_key=' + API_Key
            routerlist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json containing all of the router info
            #json_formatted_routerlist = json.dumps(routerlist, indent=2)
            #print ("\nDebug routerlist: " , json_formatted_routerlist)
            #build the text menu for the routers
            user_input = ''
            input_message = "Select a router:\n"
            index = 0
            for key in routerlist:
                index += 1
                routername = routerlist[key]['name']
                input_message += f'{index}) {routername}\n'
            input_message += 'You selected router: '
            #prompt for the router by number x) 
            user_input = input(input_message)
            #
            #find the router name and the position
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerposition = routerlist[key]['position_id']
                    routerflowip = routerlist[key]['router']['flow_ip']
            # now have the user select the router interface they want to enable/disable from a list
            url = 'https://' + cluster_fqdn + '/dimension/interfaces/positions?filter=(interface:router_pos_id,=,' + str(routerposition) + ')&attributes=(*)&api_key=' + API_Key
            routerinterfacelist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json containing all of the router info
            json_formatted_routerinterfacelist = json.dumps(routerinterfacelist, indent=2)
            #print ("\nDebug routerinterfacelist: " , json_formatted_routerinterfacelist)
            #count the existing interfaces t/f/[blank]
            print ("Counting the t/f/[blank] interfaces for the router ", routername)
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active, COUNT(*) from \"Interfaces\" where _interface_router_pos_id=" + str(routerposition) + " group by active;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )
            print("\nHow do you want me to set active)")
            print("\nHow do you want me to set the active parameter for all of router" + routername + " interfaces)")
            user_input = input("Input true or false any other key makes no change:")
            if user_input == 'true':
                print ("setting to active=true for all interfaces on router " + routername + ". I used this comand")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'update \"Interfaces\" set active='true' where _interface_router_pos_id=" + str(routerposition) + ";'")
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            elif user_input == 'false':
                print ("setting to active=false for all interfaces on router " +routername + ". I used this comand")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'update \"Interfaces\" set active='false' where _interface_router_pos_id=" + str(routerposition) + ";'") 
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing")
            #recount the existing interfaces t/f/[blank]
            print ("Re-counting the t/f/[blank] interfaces for the router ", routername)
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active, COUNT(*) from \"Interfaces\" where _interface_router_pos_id=" + str(routerposition) + " group by active;'")
            os.system(mycmd)
        elif(ch == 11):
            print ("Count the 'active' settings t/f/[blank] on all interfaces on all routers")
            print ("Counting the t/f/[blank] interfaces for all routers")
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active, COUNT(*) from \"Interfaces\" group by active;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )

        elif(ch == 12):
            print ("Set all interfaces on all routers to active true/false (receiving flow)")
            print ("Counting the t/f/[blank] interfaces for all routers ")
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active, COUNT(*) from \"Interfaces\" group by active;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )
            print("\nHow do you want me to set active)")
            print("\nHow do you want me to set the active parameter for all interfaces on all routers")
            user_input = input("Input true or false any other key makes no change:")
            if user_input == 'true':
                print ("setting to active=true for all interfaces on all routers ")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'update \"Interfaces\" set active='true';'")
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            elif user_input == 'false':
                print ("setting to active=false for all interfaces on all routers")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'update \"Interfaces\" set active='false';'") 
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing")
            #recount the existing interfaces t/f/[blank]
            print ("Re-counting the t/f/[blank] interfaces for all routers ")
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active, COUNT(*) from \"Interfaces\" group by active;'")
            os.system(mycmd)
        elif(ch == 13):
            print ("Overwrite a specified routers interface name, intended for config rules (works but then gets reset to router name + ifname )")
            print ("this works, name and display_name change. However on the next update they are set back to the router name + ifname by the system")
            #first get a router from the list
            #start by listing all routers and askign the user to pick one 
            url = 'https://' + cluster_fqdn + '/dimension/router/positions?attributes=*&api_key=' + API_Key
            routerlist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json containing all of the router info
            #json_formatted_routerlist = json.dumps(routerlist, indent=2)
            #print ("\nDebug routerlist: " , json_formatted_routerlist)
            #build the text menu for the routers
            user_input = ''
            input_message = "Select a router:\n"
            index = 0
            for key in routerlist:
                index += 1
                routername = routerlist[key]['name']
                input_message += f'{index}) {routername}\n'
            input_message += 'You selected router: '
            #prompt for the router by number x) 
            user_input = input(input_message)
            #
            #find the router name and the position
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerposition = routerlist[key]['position_id']
                    routerflowip = routerlist[key]['router']['flow_ip']
            # now have the user select the router interface they want to enable/disable from a list
            url = 'https://' + cluster_fqdn + '/dimension/interfaces/positions?filter=(interface:router_pos_id,=,' + str(routerposition) + ')&attributes=(*)&api_key=' + API_Key
            routerinterfacelist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json containing all of the router info
            json_formatted_routerinterfacelist = json.dumps(routerinterfacelist, indent=2)
            #print ("\nDebug routerinterfacelist: " , json_formatted_routerinterfacelist)
            #build the text menu for the router interfaces
            user_input = ''
            input_message = "Select an interface from that router:\n"
            index = 0
            for key in routerinterfacelist:
                index += 1
                interfacename = routerinterfacelist[key]['name']
                input_message += f'{index}) {interfacename}\n'
            input_message += 'You selected router interface: '
            #prompt for the router interface by number x) 
            user_input = input(input_message)
            #find the interface position and name 
            index = 0
            for key in routerinterfacelist:
                index += 1
                if index == int(user_input):
                    #get the name of the selected interface
                    interfacenameselected = routerinterfacelist[key]['name']
                    #get the position of the selected interface
                    interfacepositionselected = routerinterfacelist[key]['id']
                    #get the json for the selected interface
                    routerinterfaceselectedjson = routerinterfacelist[key]
                    #print ("Debug: interfacenameselected=", interfacenameselected)
                    #print ("Debug: interfacepositionselected=", interfacepositionselected)
                    #print ("Debug: routerinterfaceselectedjson=", routerinterfaceselectedjson)
            print ("\nThe interfaces dimension api is buggy (5.4), doesn't allow us to set an interface name")
            print ("\nhowever its the name we need for config rules, as the name is infact the description")
            print ("So we are going to have to do this directly in postgress (5.4+)")
            print ("You selected router ", routername)
            print ("You selected interface ", interfacenameselected)
            print ("The interfaces current setting for name is\n-------")
            mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select name from \"Interfaces\" where id=" + str(interfacepositionselected) + " order by id;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )
            print("\nHow do you want me to this interfaces name")
            user_input = input("Input a text string or hit enter to do nothing at all:")
            #if user_input != '':
            if(len(user_input) != 0):
                print ("setting the name, I used this comand")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c \"update \\\"Interfaces\\\" set name='" + user_input + "' where id=" + str(interfacepositionselected) + ";\"")
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing")
            print ("The interfaces current setting for name is now\n-------")
            mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select name from \"Interfaces\" where id=" + str(interfacepositionselected) + " order by id;'")
            os.system(mycmd)
        elif(ch == 14):
            print ("To Debug check syslog: sudo less /var/log/syslog")
            print ("Example Output below")
            print ("but 200 OK just means the json was ok. If it fails to add its silent")
            print ("")
            print ("")
            print ("Dec 15 19:48:39 master home.py[95936][INFO]: 200 POST /api/devices/topology?api_key=************ (127.0.0.1) 1284.48ms")
            print ("Dec 15 19:48:39 master home.py[95936][INFO]: Request to /api/devices/topology?api_key=************ completed in 1.284 seconds. 0 bytes were transferred.")
            print ("Dec 15 19:48:39 master home.py[95936][INFO]: /api/devices/topology?api_key=************ took 1 seconds to load for User 4acd26f26fa54fbbe02394be699dcd41bc9b1990 Status: 200")
        elif(ch == 15):
            print ("================================================================================")
            print ("Procedure to change any fields in an existing router/dms using the dimensions api")
            print ("================================================================================")
            print ("This is the simplest method I've found for now, as it preserved the passwords and hidden fields")
            print ("I'll code it up when I get time")
            print ("")
            print ("#get the dimension number for the router dimension")
            print ("curl -k --silent -X GET 'https://localhost/dimensions/index?&api_key=31UO2fiKwinzYl' | grep -e dimension_id -e \"\\\"name\\\"\" | grep -B 1 router")
            print ("")
            print ("Example: ")
            print ("    \"dimension_id\": 115,")
            print ("    \"name\": \"router\",")
            print ("")
            print ("#get the possition id for your router ")
            print ("curl --silent --insecure -X GET 'https://localhost/dimension/router/positions?&attributes=(*)&api_key=31UO2fiKwinzYl' | grep -e position_id -e \"\\\"name\\\"\" ")
            print ("")
            print ("Example:")
            print ("    \"name\": \"vDMS_172.31.200.227_3\",")
            print ("    \"position_id\": 4,")
            print ("")
            print ("#grab the router json and extract the possition (example router dimension=115, example possition=4)")
            print ("zcat /pipedream/cache/dimensions/router.json.gz | jq '.dimensions.\"115\".positions.\"4\"' > modified-router.json")
            print ("")
            print ("#delete this line to avoid an api bug")
            print ("sed -i '/\\\"snmp_ip\\\"/d' modified-router.json")
            print ("")
            print ("#Modify the file modified-router.json parameters as you need ")
            print ("")
            print ("#update the router using the dimensions api")
            print ("curl --insecure -X POST --data-binary '@modified-router.json' https://localhost/api/router/4?api_key=31UO2fiKwinzYl")
            print ("")
            print ("")
        elif(ch == 16):
            print ("================================================================================")
            print ("Procedure to create a new router/dms from an existing router/dms using the  dimension/router api")
            print ("================================================================================")
            print ("This is the simplest method I've found for now, as it preserved the passwords and hidden fields")
            print ("I'll code it up when I get time")
            print ("")
            print ("#get the dimension number for the router dimension")
            print ("curl -k --silent -X GET 'https://localhost/dimensions/index?&api_key=31UO2fiKwinzYl' | grep -e dimension_id -e \"\\\"name\\\"\" | grep -B 1 router")
            print ("")
            print ("Example: ")
            print ("    \"dimension_id\": 115,")
            print ("    \"name\": \"router\",")
            print ("")
            print ("#get the possition id for existing router you want to create your new router from")
            print ("curl --silent --insecure -X GET 'https://localhost/dimension/router/positions?&attributes=(*)&api_key=31UO2fiKwinzYl' | grep -e position_id -e \"\\\"name\\\"\" ")
            print ("")
            print ("Example:")
            print ("    \"name\": \"vDMS_172.31.200.227_3\",")
            print ("    \"position_id\": 4,")
            print ("")
            print ("#grab the existing router json and extract the possition (example router dimension=115, example possition=4)")
            print ("zcat /pipedream/cache/dimensions/router.json.gz | jq '.dimensions.\"115\".positions.\"4\"' > modified-router.json")
            print ("")
            print ("#delete this line to avoid an api bug")
            print ("sed -i '/\\\"snmp_ip\\\"/d' modified-router.json")
            print ("")
            print ("#Modify the file modified-router.json parameters")
            print ("#position_id needs to be any free possition")
            print ("#change the name")
            print ("#change the other fields as you need")
            print ("")
            print ("#add your new router/dms")
            print ("curl --insecure 'https://localhost/dimension/router/position/create?api_key=31UO2fiKwinzYl' --data-binary @modified-router.json")
            print ("")
            print ("")
        elif(ch == 17):
            print("Dump the udms mdms configs using /api/devices/dms")
            mycmd = ("curl --insecure -X GET 'https://" + cluster_fqdn + "/api/devices/dms?&attributes=(*)&api_key=" + API_Key + "' | json_pp | tee dmslist.json")
            print("Command is:" + mycmd )
            input("\nPress enter to run the command")
            os.system(mycmd)
            print("\n\nI've written the output to file dmslist.json for you")
        elif(ch == 18):
            print("Delete a router selected from a list of all routers")
            url = 'https://' + cluster_fqdn + '/dimension/router/positions?attributes=*&api_key=' + API_Key
            routerlist = requests.get(url, verify=False).json()
            json_formatted_routerlist = json.dumps(routerlist, indent=2)
            #for debug the line below prints the json
            #print ("\nDebug routerlist: " , json_formatted_routerlist)
            #build the text menu
            user_input = ''
            input_message = "Select a router:\n"
            index = 0
            for key in routerlist:
                index += 1
                routername = routerlist[key]['name']
                input_message += f'{index}) {routername}\n'
            input_message += 'You selected router: '
            #prompt for the router by number x) 
            user_input = input(input_message)
            #now find the selected router name and position for the selected number
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerposition = routerlist[key]['position_id']
            print ("You selected Router name:", routername)
            print ("That Router has position:", routerposition)
            print ("The following command will delete the selected router")
            mycmd = ("curl --insecure -X DELETE 'https://" + cluster_fqdn + "/api/router/" + str(routerposition) + "?api_key=" + API_Key + "'")
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will delete the router for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\n\nAll Done")
        elif(ch == 19):
            topmenu()
        else:
            print("Invalid entry")
        input("\nPress enter to continue")
        os.system("clear")
        submenu216()

def submenu217():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tData Views")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Get the data view API Topology Schema
            2.For an example traffic query, show me how to find the data view that was used
            3.Get a list of all data views via the API, write to a file (this is a big list, perhaps the next one is better)
            4.Dump a specific data view, selected from a menu of all configured data views 
            5.Example Case:Create a new custom ddos data view for regs (high retention) - A step by step using an example
            6.Example Case: Create a new custom ddos data view sliced on a custom protection group - A step by step using an example
            7.Create a new data view from a json file - A step by step
            8.Patch an existing data view retention - A step by step
            9.PUT (update) the fields of a dataview from a json file - A step by step
            10.Delete an existing data view
            11.Log the current calculated disk space for each data view 
            12.Configure a daily CRON job to log the current calculated disk space for each data view to /pipedream/log/
            13.Remove the daily CRON job to log the current calculated disk space for each data view
            14.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            print("To see the data view API Schema, point your browser here ")
            mycmd = ("curl --insecure --silent -X OPTIONS 'https://" + cluster_fqdn + "/api/data_views/?api_key=" + API_Key + "' | json_pp | tee dataviewschema.json")
            os.system(mycmd)
            print("Command was:" + mycmd )
            print("\n\nI've written the schema output to file dataviewschema.json for you")
        elif(ch == 2):
            print("-------------------------")
            print("For an example traffic query, show me how to find the data view that was used")
            print("-------------------------")
            print("Lets take the following simple query,\n   15 minutes of traffic\n   dimensions=timestamp&sites\n   top 100\n   output format csv")
            mycmd = ("curl -k -X GET 'https://" + cluster_fqdn + "/cube/traffic.csv?slice=timestamp(-15minutes:now)&dimensions=timestamp,sites&measures=sum.total.bytes&api_key=" + API_Key + "&a=top(auto,n:100)'")
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("-------------------------")
            print("In order to find the data view the system used we just need to modify our query to json and grep for view_name")
            print("Hint: For very long query results json_pp can hang, in which case use jq . instead")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/cube/traffic.json?slice=timestamp(-15minutes:now)&dimensions=timestamp,sites&measures=sum.total.bytes&api_key=" + API_Key + "&a=top(auto,n:100)' | json_pp | grep view_name")
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("----all done-------")
        elif(ch == 3):
            print ("Get a list of all data views via the data view API, write to a file (this is a big list, perhaps the next one is better)")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/data_views/?api_key=" + API_Key + "' | json_pp | tee dataviewsdump.json") 
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("I've send the output to file dataviewsdump.json")
        elif(ch == 4):
            print("Dump a specific data view, selected from a menu of all configured data views")
            #url = 'https://' + cluster_fqdn + '/dimension/router/positions?api_key=' + API_Key
            url = 'https://' + cluster_fqdn + '/api/data_views/?attributes=*&api_key=' + API_Key
            dataviewlist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json
            json_formatted_dataviewlist = json.dumps(dataviewlist, indent=2)
            #print ("\nDebug dataviewlist: " , json_formatted_dataviewlist)
            #build the text menu
            user_input = ''
            input_message = "Select a data view:\n"
            index = 0
            for key in dataviewlist['data']:
                index += 1
                #print ("DEBUG: key:", key)
                dataviewname = key['name']
                dataviewuuid = key['uuid']
                #print ("DEBUG: dataviewname:", dataviewname)
                #print ("DEBUG: dataviewuuid:", dataviewuuid)
                input_message += f'{index}) {dataviewname}\n'
            input_message += 'You selected data view: '
            #prompt for the data view by number x) 
            user_input = input(input_message)
            #now find the selected dataview name and uuid for the selected number
            index = 0
            for key in dataviewlist['data']:
                index += 1
                if index == int(user_input):
                    dataviewname = key['name']
                    dataviewuuid = key['uuid']
            print ("You selected data view name:", dataviewname)
            print ("Grabbing the dataview details for you")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/data_views/" + dataviewuuid + "?api_key=" + API_Key + "' | json_pp | tee mydataview.json") 
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("\n\nI've written the output to file mydataview.json for you")
        elif(ch == 5):
            print("Example case: Create a new custom ddos data view for regs (long retention) - A step by step")
            url = 'https://' + cluster_fqdn + '/api/data_views/?attributes=*&api_key=' + API_Key
            CustomDDOSDataView = """{
   "timestep_retention_days" : {
      "10s" : 7,
      "5min" : 7,
      "30min" : 7,
      "2hour" : 7,
      "day" : 7 
   },
   "context" : "traffic",
   "slice" : {
      "category" : {
         "values" : [
            "ddos"
         ],
         "type" : "include"
      }
   },
   "name" : "custom-user-ddos-slice",
   "description" : "Long Retention DDOS traffic for regs",
   "comment" : "Creating a view for regs",
   "source_timestep" : "10s",
   "dimensions" : [
      {
         "split" : "src",
         "base" : "origin_asn"
      },
      {
         "base" : "protocol"
      },
      {
         "base" : "protectiongroup",
         "split" : "dst"
      },
      {
         "base" : "tcpflags"
      },
      {
         "base" : "avg_packet_size"
      },
      {
         "base" : "suspicious"
      },
      {
         "base" : "category"
      },
      {
         "split" : "src",
         "base" : "country"
      },
      {
         "base" : "ddos"
      },
      {
         "base" : "manual_ddos_ruleset"
      },
      {
         "base" : "manual_ddos_policy"
      },
      {
         "base" : "addr",
         "split" : "dst"
      },
      {
         "split" : "src",
         "base" : "addr"
      },
      {
         "base" : "all_boundary_columns_macro"
      },
      {
         "split" : "dst",
         "base" : "port"
      },
      {
         "split" : "src",
         "base" : "port"
      }
   ]
}
"""
            print ("\n\nPrinting the JSON ddos example\n", CustomDDOSDataView)
            print ("\n\nWriting the JSON ddos example to file ddos-baseline-example.json\n\n")
            with open('ddos-baseline-example.json', 'w') as f:
               f.write(str(CustomDDOSDataView))   
            print ("\n\nThe following command will create the new ddos dataview")
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@ddos-baseline-example.json' https://" + cluster_fqdn + "/api/data_views/?api_key=" + API_Key)
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will create the dataview for you, any other key to do nothing at all:")
            if user_input == 'yes':
            #if(len(user_input) != 0):
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing. You can use the curl above to create the dataview yourself")
        elif(ch == 6):
            print("Example case: Create a new custom ddos data view sliced on a custom protection group - A step by step")
            url = 'https://' + cluster_fqdn + '/api/data_views/?attributes=*&api_key=' + API_Key
            CustomDDOSDataView = """{
   "timestep_retention_days" : {
      "5min" : 30 
   },
   "context" : "traffic",
   "source_timestep" : "10s",
   "slice" : {
      "ExampleCustomProtectedObject.dst" : {
         "type" : "exclude",
         "values" : [
            "0"
         ]
      },
      "category" : {
         "type" : "include",
         "values" : [
            "ddos"
         ]
      }
   },
   "name" : "Example-Dataview-ingress-ddos-analysis",
   "description" : "DDOS traffic details sliced against a custom protection group",
   "comment" : "Creating a view to help with ddos analysis",
   "dimensions" : [
      {
         "split" : "src",
         "base" : "origin_asn"
      },
      {
         "base" : "protocol"
      },
      {
         "base" : "ExampleCustomProtectedObject",
         "split" : "dst"
      },
      {
         "base" : "tcpflags"
      },
      {
         "base" : "category"
      },
      {
         "split" : "src",
         "base" : "country"
      },
      {
         "base" : "ddos"
      },
      {
         "base" : "addr",
         "split" : "dst"
      },
      {
         "split" : "src",
         "base" : "addr"
      },
      {
         "base" : "all_boundary_columns_macro"
      },
      {
         "base" : "avg_packet_size"
      },
      {
         "base" : "max_ttl"
      },
      {
         "base" : "min_ttl"
      },
      {
         "split" : "dst",
         "base" : "port"
      },
      {
         "split" : "src",
         "base" : "port"
      }
   ]
}
"""
            print ("\n\nPrinting the JSON ddos example\n", CustomDDOSDataView)
            print ("\n\nWriting the JSON ddos example to file ddos-baseline-example.json\n\n")
            with open('ddos-baseline-example.json', 'w') as f:
               f.write(str(CustomDDOSDataView))   
            print ("\n\nThe following command will create the new ddos dataview")
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@ddos-baseline-example.json' https://" + cluster_fqdn + "/api/data_views/?api_key=" + API_Key)
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will create the dataview for you, any other key to do nothing at all:")
            if user_input == 'yes':
            #if(len(user_input) != 0):
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\n\nGive it an hour and the following example query should hit your new dataview")
                print("\ncurl -k --silent -X GET 'https://" + cluster_fqdn + "/cube/traffic.json?slice=timestamp(-60minutes:now)&dimensions=timestamp,ddos,origin_asn.src,max_ttl,min_ttl,protocol,tcpflags,category,country.src,addr.src,addr.dst,port.src,port.dst&measures=avg.bps,pctl95.bps,percent_total(sum.bytes)&apply=sort(timestamp,asc)&apply=top(all,n:100)&apply=timestep(5min,5min)&bs=((boundary.peering.input,true))&slice:or=(ExampleCustomProtectedObject.dst!(None))&slice:or=(category(12))&api_key=31UO2fiKwinzYl' | jq . | grep view_name")
                print("\nAll Done")
            else:
                print ("doing nothing. You can use the curl above to create the dataview yourself")
        elif(ch == 7):
            print("Create a new dataview from a json file - A step by step")
            print("hint1: build data views with 10s and 2min timesteps with a source_timestep of 10s")
            print("hint2: build data views with 30min, 2hr and day timesteps from a parent view with a 5min timestamp and the same dimensions, base_view for example. you cannot use 10s")
            data_view_filename = input("enter the json filename to import the data view from:")
            print("\n\nThe following command will add the JSON in order to create a new data view")
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@" + data_view_filename + "' https://" + cluster_fqdn + "/api/data_views/?api_key=" + API_Key)
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will create the data view for you, any other key to do nothing at all:")
            if user_input == 'yes':
            #if(len(user_input) != 0):
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing. You can use the curl above to create the data view yourself")
        elif(ch == 8):
            print("Patch an existing data view retention - A step by step")
            url = 'https://' + cluster_fqdn + '/api/data_views/?attributes=*&api_key=' + API_Key
            dataviewlist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json
            json_formatted_dataviewlist = json.dumps(dataviewlist, indent=2)
            user_input = ''
            input_message = "Select a data view:\n"
            index = 0
            for key in dataviewlist['data']:
                index += 1
                #print ("DEBUG: key:", key)
                dataviewname = key['name']
                dataviewuuid = key['uuid']
                lastmodified = key['last_modified']
                #print ("DEBUG: dataviewname:", dataviewname)
                #print ("DEBUG: dataviewuuid:", dataviewuuid)
                #print ("DEBUG: lastmodified:", lastmodified)
                input_message += f'{index}) {dataviewname}\n'
            input_message += 'You selected data view: '
            #prompt for the data view by number x) 
            user_input = input(input_message)
            #now find the selected data view name and uuid for the selected number
            index = 0
            for key in dataviewlist['data']:
                index += 1
                if index == int(user_input):
                    dataviewname = key['name']
                    dataviewuuid = key['uuid']
            print ("You selected data view name:", dataviewname)
            #print ("DEBUG: lastmodified:", lastmodified)
            print ("Dumping the current data view JSON for this view")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/data_views/" + dataviewuuid + "?api_key=" + API_Key + "' | json_pp | tee example_dataview.json") 
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("\n\nLets change the retention days\n")
            input_10s = input("Enter the retention for 10s data (in days) or leave blank to not change 10s data:")
            input_5min = input("Enter the retention for 5min data (in days) or leave blank to not change 5min data:")
            input_30min = input("Enter the retention for 30min data (in days) or leave blank to not change 30min data:")
            input_2hour = input("Enter the retention for 2hour data (in days) or leave blank to not change 2hour data:")
            input_day = input("Enter the retention for day data (in days) or leave blank to not change day data:")
            json_header = "{\n   \"elements\" : ["
            if(len(input_10s) != 0):
                 json_10s = "\n      {\n        \"uuid\" : \"" + dataviewuuid + "\",\n        \"timestep\" : \"10s\",\n        \"retention_days\" : " + input_10s + ",\n        \"last_modified\" : \"" + lastmodified + "\"\n      }," 
            else:
                 json_10s = "" 
            if(len(input_5min) != 0):
                 json_5min = "\n      {\n        \"uuid\" : \"" + dataviewuuid + "\",\n        \"timestep\" : \"5min\",\n        \"retention_days\" : " + input_5min + ",\n        \"last_modified\" : \"" + lastmodified + "\"\n      }," 
            else:
                 json_5min = "" 
            if(len(input_30min) != 0):
                 json_30min = "\n      {\n        \"uuid\" : \"" + dataviewuuid + "\",\n        \"timestep\" : \"30min\",\n        \"retention_days\" : " + input_30min + ",\n        \"last_modified\" : \"" + lastmodified + "\"\n      }," 
            else:
                 json_30min = "" 
            if(len(input_2hour) != 0):
                 json_2hour = "\n      {\n        \"uuid\" : \"" + dataviewuuid + "\",\n        \"timestep\" : \"2hour\",\n        \"retention_days\" : " + input_2hour + ",\n        \"last_modified\" : \"" + lastmodified + "\"\n      }," 
            else:
                 json_2hour = "" 
            if(len(input_day) != 0):
                 json_day = "\n      {\n        \"uuid\" : \"" + dataviewuuid + "\",\n        \"timestep\" : \"day\",\n        \"retention_days\" : " + input_day + ",\n        \"last_modified\" : \"" + lastmodified + "\"\n      }," 
            else:
                 json_day = "" 
            json_tail = "\n   ],\n   \"comment\" : \"Adjusting retention of data view " + dataviewname + "\"\n}"
            #remove the last occurance of  }, in the json, replace with a }
            strValue = json_header + json_10s + json_5min + json_30min + json_2hour + json_day + json_tail
            strToReplace = "      },"
            replacementStr = "      }"
            # Reverse the substring that need to be replaced
            strToReplaceReversed   = strToReplace[::-1]
            # Reverse the replacement substring
            replacementStrReversed = replacementStr[::-1]
            # Replace last occurrences of substring 'is' in string with 'XX'
            strValue = strValue[::-1].replace(strToReplaceReversed, replacementStrReversed, 1)[::-1]
            #print("DEBUG: strValue\n", strValue)
            print("\n\nWriting the patch configuration to file patch-data-view.json")
            #file = open("patch-data-view.json", "w")
            #file.write(strValue)
            #file.close
            with open('patch-data-view.json', 'w') as f:
                f.write(strValue)
            print("\n\nThe following command will patch the data view retention")
            mycmd = ("curl --insecure -X PATCH -H 'Content-Type: application/json' -d '@patch-data-view.json' https://" + cluster_fqdn + "/api/data_views/?api_key=" + API_Key)
            print("\nCommand is:" + mycmd )
            user_input = input("\nInput yes and I will create the data view for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing. You can use the curl above to create the data view yourself")
        elif(ch == 9):
            print("PUT (Update) an existing data views fields - A step by step")
            url = 'https://' + cluster_fqdn + '/api/data_views/?attributes=*&api_key=' + API_Key
            dataviewlist = requests.get(url, verify=False).json()
            #for debug the two lines below prints the json
            json_formatted_dataviewlist = json.dumps(dataviewlist, indent=2)
            user_input = ''
            input_message = "Select a data view:\n"
            index = 0
            for key in dataviewlist['data']:
                index += 1
                #print ("DEBUG: key:", key)
                dataviewname = key['name']
                dataviewuuid = key['uuid']
                lastmodified = key['last_modified']
                #print ("DEBUG: dataviewname:", dataviewname)
                #print ("DEBUG: dataviewuuid:", dataviewuuid)
                #print ("DEBUG: lastmodified:", lastmodified)
                input_message += f'{index}) {dataviewname}\n'
            input_message += 'You selected data view: '
            #prompt for the data view by number x) 
            user_input = input(input_message)
            #now find the selected data view name and uuid for the selected number
            index = 0
            for key in dataviewlist['data']:
                index += 1
                if index == int(user_input):
                    dataviewname = key['name']
                    dataviewuuid = key['uuid']
            print ("You selected data view name:", dataviewname)
            #print ("DEBUG: lastmodified:", lastmodified)
            print ("Dumping the current data view JSON for this view to file dataview_before_being_modified.json")
            mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/data_views/" + dataviewuuid + "?api_key=" + API_Key + "' | json_pp | tee dataview_before_being_modified.json") 
            print("Command is:" + mycmd )
            os.system(mycmd)
            print ("Making a copy of file 'dataview_before_being_modified.json' to file 'dataview_after_being_modified.json'")
            mycmd = ("cp dataview_before_being_modified.json dataview_after_being_modified.json")
            os.system(mycmd)
            print("##########################################################################")
            print("Now in a different window go and modify the file 'dataview_after_being_modified.json'")
            print("Add or delete or update the fields as you need to")
            print("You will also have to change the json block \"timesteps\" : {")
            print("Into a json block structured like this,..")
            print("   \"timestep_retention_days\" : {")
            print("       \"5min\" : x,")
            print("       \"2hour\" : x,")
            print("       \"week\" : x")
            print("   },")
            print("You will also need to add a comment block..something like")
            print("\"comment\": \"Modifying fields as requested by customer\"")
            print("Then hit enter to load the file and modify the dataview fields")
            print("##########################################################################")
            user_input = input("hit [enter] once you are ready:")
            print("\n\nThe following command will update the dataview with your modified json file")
            mycmd = ("curl --insecure -X PUT -H 'Content-Type: application/json' -d '@dataview_after_being_modified.json' https://" + cluster_fqdn + "/api/data_views/" + dataviewuuid + "?api_key=" + API_Key)
            print("\nCommand is:" + mycmd )
            user_input = input("\nInput yes and I will create the data view for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print ("Dumping the dataview json again to file 'dataview_final_check.json'")
                mycmd = ("curl -k --silent -X GET 'https://" + cluster_fqdn + "/api/data_views/" + dataviewuuid + "?api_key=" + API_Key + "' | json_pp | tee dataview_final_check.json") 
                os.system(mycmd)
                print ("As a final validation:")
                print ("Running a diff of the dataview json now verses before the changes")
                print ("Besides the changes you made, we only expect to see last_modified showing up in here")
                mycmd = ("diff dataview_final_check.json dataview_before_being_modified.json") 
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing. You can use the curl above to update the data view yourself")
        elif(ch == 10):
            print ("Delete an existing data view")
            url = 'https://' + cluster_fqdn + '/api/data_views/?attributes=*&api_key=' + API_Key
            dataviewlist = requests.get(url, verify=False).json()
            json_formatted_dataviewlist = json.dumps(dataviewlist, indent=2)
            user_input = ''
            input_message = "Select a data view:\n"
            index = 0
            for key in dataviewlist['data']:
                index += 1
                #print ("DEBUG: key:", key)
                dataviewname = key['name']
                dataviewuuid = key['uuid']
                #print ("DEBUG: dataviewname:", dataviewname)
                #print ("DEBUG: dataviewuuid:", dataviewuuid)
                input_message += f'{index}) {dataviewname}\n'
            input_message += 'You selected data view: '
            #prompt for the data view by number x) 
            user_input = input(input_message)
            #now find the selected data view name and uuid for the selected number
            index = 0
            for key in dataviewlist['data']:
                index += 1
                if index == int(user_input):
                    dataviewname = key['name']
                    dataviewuuid = key['uuid']
            print ("You selected data view name:", dataviewname)
            print("\n\nThe following command will delete that data view")
            #mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@example_dataview.json' https://" + cluster_fqdn + "/api/data_views/?api_key=" + API_Key)
            mycmd = ("curl -k --silent -X DELETE 'https://" + cluster_fqdn + "/api/data_views/" + dataviewuuid + "?api_key=" + API_Key + "' ")
            print("Command is:" + mycmd )
            user_input = input("WARNING: Input yes and I will delete the data view for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing. You can use the curl above to delete the data view yourself")
        elif ch == 11:
            print ("Logging the current calculated disk space for each data view")
            print ("Appending the output to files {} and {}".format(str(disk_space_filename_sorted),str(disk_space_filename)))
            mycmd = ("python3 log_dataview_size.py " + cluster_fqdn + " " + API_Key + " -log_dir .")
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 12:
            print ("Install a daily cron on mast to log the current calculated disk space each data view to /pipedream/log/")
            input("\nPress enter to continue")
            mycmd = ("sudo cp log_dataview_size.py /usr/local/sbin/log_dataview_size.py")
            os.system(mycmd)
            mycmd = ("sudo chmod a+x /usr/local/sbin/log_dataview_size.py")
            os.system(mycmd)
            mycmd = ("(crontab -l 2>/dev/null; echo \"0 1 * * * /usr/bin/python3 /usr/local/sbin/log_dataview_size.py localhost " + API_Key + " -log_dir /pipedream/log/\") | crontab -")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print ("The cron will log dataview sizes once a day to /pipedream/log/{} and /pipedream/log/{}".format(str(disk_space_filename_sorted),str(disk_space_filename)))
        elif ch == 13:
            print ("Remove the daily cron on master to log the current calculated disk space each data view")
            input("\nPress enter to continue")
            mycmd = ("crontab -l 2>/dev/null | grep -v '/usr/local/sbin/log_dataview_size.py'  | crontab -")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print ("The cron job has been removed")
        elif ch == 14:
            topmenu()
        else:
            print("Invalid entry")
        input("\nPress enter to continue")
        os.system("clear")
        submenu217()
def submenu29():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Kafka (must be ran on the master)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.list the available kafka consumer groups
            2.show the kafka df-dnsflowd consumer groups
            3.show the kafka df-dnsflow-raw topic and partitions 
            4.show the kafka df-classifyd consumer groups 
            5.show the kafka df-flow topic and partitions 
            6.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycmd = "kafka-consumer-groups --bootstrap-server localhost:9092 --list"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 2):
            mycmd = "kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group df-dnsflowd"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 3):
            mycmd = "kafka-topics --bootstrap-server localhost:9092 --describe --topic df-dnsflow-raw"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 4):
            mycmd = "kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group df-classifyd"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 5):
            mycmd = "kafka-topics --bootstrap-server localhost:9092 --describe --topic df-flow"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 6:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu29()



def submenuexample():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Example")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.show the example1 on each node 
            2.show the example2 on each node 
            13.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycmd = "sudo salt \* cmd.run \"ip addr show\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif(ch == 2):
            mycmd = "sudo salt \* cmd.run \"netstat -rn\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 3:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenuexample()





def whatsatrainer():
     print("""
               /@\            \|/   
              `-\ \  ______  - 0 -   
                 \ \/ ` /  \  /|\ _   
                  \_i / \  |\____//   
                    | |==| |=----/   
              ----------------------  
              A trainer is code designed to teach how to write and execute day to day tasks and automations
              Trainer code is not fancy, as its intended to be readable. 
              It tells the user how it did the task, so they can do it themselfes 
              The code is intended to be shared, improved and reused. No rules
              Its written on top of other peoples code, thanks Ato, thanks Chris 
              Its a quick way for Deepfield Customer Engineers to get started

              To run these menu's you have to be a sudo user such as support, so the assumption is you are an experienced user 
              Regardless Menu options which change things have the ability to destroy a platform. 
              So please test and understand in vlabs prior to running in prod 
                 """)
     print("\n")
     input("Press enter to continue")
     os.system("clear")
     topmenu()

#Thanks Ato for this block, based on user_query_summary.py 
def getMostUsedQueries():
    #args = parse_args()
    makeTempDir()
    scrapeLogs(getListOfLogFiles(), False)
    ## Storing as global because it's hard to pass a value into a dataframe apply.
    global queryThreshold
    #show the top 20 queries
    queryThreshold = 20 
    reEvaluate = True 
    ## Storing all information about views in the global namespace.
    global allContextInfo
    global boundaryMap
    global allContextViewInfo
    allContextInfo = get_context.Context(contextList=mycontext, reEvaluate=True, callingProgram='Dino')
    boundaryMap = allContextInfo.boundaryMap
    allContextViewInfo = allContextInfo.allContextViewInfo
    analyzeQueries(getQueryInfoFromLogs())

def getMostUsedQueriesSubscriber():
    #args = parse_args()
    makeTempDir()
    scrapeLogs(getListOfLogFiles(), False)
    ## Storing as global because it's hard to pass a value into a dataframe apply.
    global queryThreshold
    #show the top 20 queries
    queryThreshold = 20 
    reEvaluate = True 
    ## Storing all information about views in the global namespace.
    global allContextInfo
    global boundaryMap
    global allContextViewInfo
    allContextInfo = get_context.Context(contextList=['subscriber'], reEvaluate=True, callingProgram='Dino')
    boundaryMap = allContextInfo.boundaryMap
    allContextViewInfo = allContextInfo.allContextViewInfo
    analyzeQueries(getQueryInfoFromLogs())


def getListOfLogFiles():
    filesToConsume = []
    for thisFile in os.listdir(logDir):
        if uiLogName in thisFile:
            filesToConsume.append(logDir + str(thisFile))
    log.info("Found files:" + str(filesToConsume))
    return filesToConsume

def scrapeLogs(listOfFiles=['/pipedream/log/ui.log.1'], rescrapeLogs=True):
    if os.path.exists(queriesFile) and not rescrapeLogs:
        log.info("Using existing logs. Use --force to rescrape the logs.")
        return
    elif os.path.exists(queriesFile):
        log.info("Removing existing logs.")
        os.remove(queriesFile)
    for thisFile in listOfFiles:
        log.info("Processing: " + thisFile)
        grepString = ' | grep "200 GET" | grep -v datasource | grep -v loginfo | grep -v queue=system | grep -v estimate | grep "/cube/\|count" >>'
        if thisFile.endswith('.gz'):
            cmd = 'sudo zcat ' + thisFile + grepString + queriesFile
        else:
            cmd = 'sudo cat ' + thisFile + grepString + queriesFile
        run(cmd, stderr=subprocess.STDOUT, shell=True)
    log.info("Saving query logs to " + queriesFile)


def getQueryInfoFromLogs():
    queries = []
    count = 0
    with open(queriesFile) as f:
        for line in f:
            mo = type_regex.search(line)
            if mo:
                queryType = mo.group(1)
            mo = cube_regex.search(line)
            if mo:
                cube = mo.group(1)
            mo = dim_regex.search(line)
            if mo:
                dims = mo.group(1)
            else:
                dims = ''
            # Split string in list, and then convert to set to
            # combine with dims in slice.
            dimset = set(dims.split(','))
            # Find all dims in slices, convert to set,and than combine with
            # dimset to get unique list of all dims in query.
            sliceset = set(slice_regex.findall(line))
            alldimset = dimset | sliceset
            # Next line removes the 'timestamp' dim to simplify query-summary.
            alldimset = {x.replace('timestamp', '') for x in alldimset}
            # Next line will remove empty strings in case
            # no dim was found in the query.
            alldimset = list(filter(None, alldimset))
            # Apply similar logic to extract the boundaries
            boundarysliceset = set(boundaryslice_regex.findall(line))
            boundarysliceset = list(filter(None, boundarysliceset))
            boundaries = list()
            if len(boundarysliceset) == 0:
                boundaries = []
            else:
                for boundaryslice in boundarysliceset:
                    mo = boundary_regex.search(boundaryslice)
                    if mo:
                         boundaries.append(mo.group(1).lower())
            mo = timestamp_regex.search(line)
            if mo:
                timestamp = mo.group(1)
            else:
                timestamp = ''
            mo = apikey_regex.search(line)
            if mo:
                apikey = mo.group(1)
            else:
                apikey = ''
            queries.append((queryType, cube, tuple(sorted(alldimset)), tuple(sorted(boundaries)), timestamp, apikey))
            count = count+1
    log.info('Processing ' + str(count) + ' queries.')
    pd.set_option('display.max_colwidth', -1)
    queriesDataFrame = pd.DataFrame(queries, columns =['type', 'context', 'dimensions', 'boundaries', 'timestamp', 'apikey'])
    return queriesDataFrame

def analyzeQueries(queriesDF):
    supportKeys = deepy.deepui.get_root_api_keys()
    contextsToEvaluate = mycontext 
    #exclude queries made by the support user as thats us not the customer
    log.info("Removing the Support user queries and doing some math.")
    slicedQueries = queriesDF.query("context == @contextsToEvaluate and apikey != @supportKeys")
    #count the queries
    countedQueries = slicedQueries.groupby(["context", "dimensions", "boundaries"])["context", "dimensions", "boundaries"]\
        .size().to_frame('count').reset_index()
    log.info("Mapping view UUID to queries.")
    taggedQueries = countedQueries.apply(allContextInfo.view_uuid, axis=1)
    taggedQueries.to_csv(querySummaryfile, sep=';', index=False)

    csvData = pd.read_csv(querySummaryfile, delimiter = ";")
    csvData.sort_values(["count"], 
                    axis=0,
                    ascending=[False], 
                    inplace=True)
    # write query sorted data to file  
    csvData.to_csv(querySummaryfileSorted, sep=';', index=False)
    # print a summary to the screen, along with where to find the detailed files 
    print("\n\n*************************************************************")
    print("Printing a summary of file querysummary_sorted_on_count.csv, just the first 20 queries for each dimension, essential fields")
    for aContext in contextsToEvaluate:
        print("*************************************************************")
        print(" Top queried dimensions for " + str(aContext) + ".")
        print("*************************************************************")
        df = taggedQueries.query("context == [@aContext]")
        print(df[["context", "dimensions", "boundaries", "uuid", "name", "count"]].sort_values(['count'], ascending=False).head(queryThreshold))
    print("*************************************************************")
    print("\n\nDetailed query results can be found in the following files \n")
    print("	" + WorkingDir + "dino-" + str(os.getpid()) + "/querysummary_sorted_on_count.csv contains the queries sorted on number of hits")
    print("	"  + WorkingDir + "dino-" + str(os.getpid()) + "/queries_from_logs.txt contains the log entries for all querys found")
    print("\n\nSome of the files can get quite large, so if you do not planning to use them you might consider cleanig up with \n")
    print("rm -rf " + WorkingDir + "dino-" + str(os.getpid()))


def makeTempDir():
    tmpDirPath = ( WorkingDir + 'dino-' + str(os.getpid()))  
    log.info('Creating dir ' + str(tmpDirPath))
    os.mkdir(str(tmpDirPath))
    os.chdir(tmpDirPath)

def replace_last(string, old, new):
    return new.join(string.rsplit(old, 1))

def get_api_key():
    if RunningOnMaster == 'no':
        print ("You are not running on a master node, so you will have to provide your API key manually")
        API_Key=input("Enter your API key: ")
    else: 
        #We are running on a mater node
        #So grab the first API key from the support users list of keys using deepy
        API_Keys = deepy.deepui.get_root_api_keys()
        API_Key = API_Keys[0]
        #check its really set, if not ask for a manualy entered key
        if not API_Key:
            print ("I did not manage to extract your support user API key, so could you please paste it here")
            API_Key=input("Enter your API key: ")
        else: 
            print("Using the following API key for queries: " , API_Key)
    return (API_Key)

def get_cluster_fqdn():
    if RunningOnMaster == 'no':
        print ("You are not running on a master node, so you will have to provide your Deepfield clusters API fqdn manually example: mycluster.deepfield.net")
        cluster_fqdn=input("Enter your clusters fqdn: ")
        print ("Please keep in mind that while menu items using the APIs will work,  some other menu items will not work on a remote host,")
        print ("As the master nodes commands will not be available")
        input("Press any key to continue...")
    else: 
        cluster_fqdn = "localhost" 
    print("Using the following fqdn for API queries: " , cluster_fqdn)
    return (cluster_fqdn)

# Main program  
API_Key = get_api_key()
cluster_fqdn = get_cluster_fqdn()
topmenu() 

