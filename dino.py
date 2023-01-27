# importing the modules
import os
import re
import subprocess
import socket
import deepy.cfg
import deepy.deepui
import get_context
import pandas as pd
import requests 
import deepy.log as log
import json 
from subprocess import check_output as run
from datetime import date
#date 
today = str(date.today())
#statics
logDir = '/pipedream/log/'
uiLogName = 'ui.log'
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
            6.mysql (empty)
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
            18.Collect the logs and slice.json from all DCUs
            19.Exit""")
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
            os.system("date")
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
            1.Traffic reports
            2.Sub-i Reports
            3.DDoS Reports
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
    print("\tDeepfield Cluster Health")
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
            7.check the performance of collectord on each worker 	#100% indicated it is time to scale up
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
            mycmd = "sudo salt \* cmd.run \"ps -eo %mem,%cpu,pid,ppid,cmd --sort=-%mem | cut -c -140 | grep collectord | grep -v grep \""
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
    print("\tDeepfield Cluster Configuration")
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
    print("\tDeepfield Queries the customer is using most frequently (view optimization)")
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
        #to get avialable cubes https://localhost:22222/cube/list
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
    print("\tpostgres")
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
    print("\tCollecting logs and config files")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Collect log files and slice.json from all DCUs, make one large tar file on master
            2.Clean up old tar files
            3.Return""")
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
        elif ch == 2:
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
        elif ch == 3:
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

def submenu212():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Networking")
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
        elif ch == 13:
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
    print("\tDeepfield MOPS and Backups")
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
    print("\tHDFS")
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
            8.Set a specified routers interface to active true/false
            9.Overwrite a specified routers interface name, intended for config rules (works but then gets reset to router name + ifname )
            10.Debugging hints
            11.Return""")
        print("\n")
        #grab the first API key from the support users list of keys
        supportKeys = deepy.deepui.get_root_api_keys()
        firstSupportKey = supportKeys[0]
        #check its really set, if not ask for a manualy entered key
        if not firstSupportKey:
            print ("I did not manage to extract your support user API key, so could you past it here")
            firstSupportKey=input("Enter your API key: ")
        else: 
            #print("The support user API key is " , firstSupportKey)
            print("")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            print("To see the Device API Topology Schema, point your browser here ")
            print("https://" + re.sub("^[a-z]+\.", "", socket.gethostname())+ "/docs/api/devices/topology")
        elif(ch == 2):
            print("To see the Device API Utilisation Schema, point your browser here ")
            print("https://" + re.sub("^[a-z]+\.", "", socket.gethostname())+ "/docs/api/devices/utilization")
        elif(ch == 3):
            print("Method GET is as of 5.4 not supported, so this command will fail. Only POST is supported")
            print("curl --insecure -X GET 'https:/localhost/api/devices/topology?api_key=" + firstSupportKey + "'")
            print("I've provided an alternative more complex methods in the following options")
        elif(ch == 4):
            print("Get a list of routers and attributes using the routers dimension")
            mycmd = ("curl --insecure -X GET 'https://localhost/dimension/router/positions?&attributes=(*)&api_key=" + firstSupportKey + "' | tee routerlist.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("\n\nI've written the output to file routerlist.json for you")
        elif(ch == 5):
            print("Get a list of all interfaces via the interface dimension")
            mycmd = ("curl --insecure -X GET 'https://localhost/dimension/interfaces/positions?&attributes=(*)&api_key=" + firstSupportKey + "' | tee interfacelist.json")
            print("Command is:" + mycmd )
            os.system(mycmd)
            print("\n\nI've written the output to file interfacelist.json for you")
        elif(ch == 6):
            print("Get a list of interfaces for a given router via the interface dimension")
            #url = 'https://localhost/dimension/router/positions?api_key=' + firstSupportKey
            url = 'https://localhost/dimension/router/positions?attributes=*&api_key=' + firstSupportKey
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
            #now find the selected router name and possition for the selected number
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerpossition = routerlist[key]['position_id']
            print ("You selected Router name:", routername)
            print ("That Router has possition:", routerpossition)
            print ("The following command will get the router interfaces")
            mycmd = ("curl --insecure -X GET 'https://localhost/dimension/interfaces/positions?filter=(interface:router_pos_id,=," + str(routerpossition) + ")&attributes=(*)&api_key=" + firstSupportKey + "' | tee myrouterinterfacelist.json")
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
            url = 'https://localhost/dimension/router/positions?attributes=*&api_key=' + firstSupportKey
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
            #find the router name and the possition
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerpossition = routerlist[key]['position_id']
                    routerflowip = routerlist[key]['router']['flow_ip']
            #
            #get the router interfaces
            url = 'https://localhost/dimension/interfaces/positions?filter=(interface:router_pos_id,=,' + str(routerpossition) + ')&attributes=(*)&api_key=' + firstSupportKey
            routerinterfaces = requests.get(url, verify=False).json()
            #for debug the line below prints the json containing all of the router interfaces
            #print ("\nDebug url: " + url)
            #json_formatted_routerinterfaces = json.dumps(routerinterfaces, indent=2)
            #print ("\nDebug routerinterfaces: ", json_formatted_routerinterfaces)
            #
            #we have router name, routername
            #we have the router possition, routerpossition
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
            mycmd = ("curl --insecure -X POST -d '@topologyConfigFile.json' https://localhost/api/devices/topology?api_key=" + firstSupportKey)
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
            print ("Set a routers interface to active true/false (receiving flow)")
            #first get a router from the list
            #start by listing all routers and askign the user to pick one 
            url = 'https://localhost/dimension/router/positions?attributes=*&api_key=' + firstSupportKey
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
            #find the router name and the possition
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerpossition = routerlist[key]['position_id']
                    routerflowip = routerlist[key]['router']['flow_ip']
            # now have the user select the router interface they want to enable/disable from a list
            url = 'https://localhost/dimension/interfaces/positions?filter=(interface:router_pos_id,=,' + str(routerpossition) + ')&attributes=(*)&api_key=' + firstSupportKey
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
            #find the interface possition and name 
            index = 0
            for key in routerinterfacelist:
                index += 1
                if index == int(user_input):
                    #get the name of the selected interface
                    interfacenameselected = routerinterfacelist[key]['name']
                    #get the possition of the selected interface
                    interfacepossitionselected = routerinterfacelist[key]['id']
                    #get the json for the selected interface
                    routerinterfaceselectedjson = routerinterfacelist[key]
                    #print ("Debug: interfacenameselected=", interfacenameselected)
                    #print ("Debug: interfacepossitionselected=", interfacepossitionselected)
                    #print ("Debug: routerinterfaceselectedjson=", routerinterfaceselectedjson)
            print ("\nThe interfaces dimension api is buggy (5.4), doesn't allow us to set or add active")
            print ("So we are going to have to do this directly in postgress (5.4+)")
            print ("You selected router ", routername)
            print ("You selected interface ", interfacenameselected)
            print ("The interfaces current setting for active is\n-------")
            mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active from \"Interfaces\" where id=" + str(interfacepossitionselected) + " order by id;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )
            print("\nHow do you want me to set active)")
            user_input = input("Input true or false any other key makes no change:")
            if user_input == 'true':
                print ("setting to active=true. I used this comand")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'update \"Interfaces\" set active='true' where id=" + str(interfacepossitionselected) + ";'")
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            elif user_input == 'false':
                print ("setting to active=false. I used this comand")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'update \"Interfaces\" set active='false' where id=" + str(interfacepossitionselected) + ";'")
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing")
            print ("The interfaces current setting for active is now\n-------")
            mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active from \"Interfaces\" where id=" + str(interfacepossitionselected) + " order by id;'")
            os.system(mycmd)
        elif(ch == 9):
            print ("Overwrite a specified routers interface name, intended for config rules (works but then gets reset to router name + ifname )")
            print ("this works, name and display_name change. However on the next update they are set back to the router name + ifname by the system")
            #first get a router from the list
            #start by listing all routers and askign the user to pick one 
            url = 'https://localhost/dimension/router/positions?attributes=*&api_key=' + firstSupportKey
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
            #find the router name and the possition
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerpossition = routerlist[key]['position_id']
                    routerflowip = routerlist[key]['router']['flow_ip']
            # now have the user select the router interface they want to enable/disable from a list
            url = 'https://localhost/dimension/interfaces/positions?filter=(interface:router_pos_id,=,' + str(routerpossition) + ')&attributes=(*)&api_key=' + firstSupportKey
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
            #find the interface possition and name 
            index = 0
            for key in routerinterfacelist:
                index += 1
                if index == int(user_input):
                    #get the name of the selected interface
                    interfacenameselected = routerinterfacelist[key]['name']
                    #get the possition of the selected interface
                    interfacepossitionselected = routerinterfacelist[key]['id']
                    #get the json for the selected interface
                    routerinterfaceselectedjson = routerinterfacelist[key]
                    #print ("Debug: interfacenameselected=", interfacenameselected)
                    #print ("Debug: interfacepossitionselected=", interfacepossitionselected)
                    #print ("Debug: routerinterfaceselectedjson=", routerinterfaceselectedjson)
            print ("\nThe interfaces dimension api is buggy (5.4), doesn't allow us to set an interface name")
            print ("\nhowever its the name we need for config rules, as the name is infact the description")
            print ("So we are going to have to do this directly in postgress (5.4+)")
            print ("You selected router ", routername)
            print ("You selected interface ", interfacenameselected)
            print ("The interfaces current setting for name is\n-------")
            mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select name from \"Interfaces\" where id=" + str(interfacepossitionselected) + " order by id;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )
            print("\nHow do you want me to this interfaces name")
            user_input = input("Input a text string or hit enter to do nothing at all:")
            #if user_input != '':
            if(len(user_input) != 0):
                print ("setting the name, I used this comand")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c \"update \\\"Interfaces\\\" set name='" + user_input + "' where id=" + str(interfacepossitionselected) + ";\"")
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing")
            print ("The interfaces current setting for name is now\n-------")
            mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select name from \"Interfaces\" where id=" + str(interfacepossitionselected) + " order by id;'")
            os.system(mycmd)
        elif(ch == 10):
            print ("To Debug check syslog: sudo less /var/log/syslog")
            print ("Example Output below")
            print ("but 200 OK just means the json was ok. If it fails to add its silent")
            print ("")
            print ("")
            print ("Dec 15 19:48:39 master home.py[95936][INFO]: 200 POST /api/devices/topology?api_key=************ (127.0.0.1) 1284.48ms")
            print ("Dec 15 19:48:39 master home.py[95936][INFO]: Request to /api/devices/topology?api_key=************ completed in 1.284 seconds. 0 bytes were transferred.")
            print ("Dec 15 19:48:39 master home.py[95936][INFO]: /api/devices/topology?api_key=************ took 1 seconds to load for User 4acd26f26fa54fbbe02394be699dcd41bc9b1990 Status: 200")
        elif(ch == 11):
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
            1.Get the Dataview API Topology Schema
            2.For an example traffic query, show me how to find the data view that was used
            3.Get a list of all dataviews via the API, write to a file (this is a big list, perhaps the next one is better)
            4.Dump a specific data view, selected from a menu of all configured data views 
            5.Show me how to create a new data view (in progress)
            6.Show me how to patch(modify) an existing data view (in progress)
            7.Show me how to PUT(replace) an existing data view (in progress)
            8.Return""")
        print("\n")
        #grab the first API key from the support users list of keys
        supportKeys = deepy.deepui.get_root_api_keys()
        firstSupportKey = supportKeys[0]
        #check its really set, if not ask for a manualy entered key
        if not firstSupportKey:
            print ("I did not manage to extract your support user API key, so could you past it here")
            firstSupportKey=input("Enter your API key: ")
        else: 
            #print("The support user API key is " , firstSupportKey)
            print("")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            print("To see the data view API Schema, point your browser here ")
            mycmd = ("curl --insecure --silent -X OPTIONS 'https://localhost/api/data_views/?api_key=" + firstSupportKey + "' | json_pp | tee dataviewschema.json")
            os.system(mycmd)
            print("Command was:" + mycmd )
            print("\n\nI've written the schema output to file dataviewschema.json for you")
        elif(ch == 2):
            print("-------------------------")
            print("For an example traffic query, show me how to find the data view that was used")
            print("-------------------------")
            print("Lets take the following simple query,\n   15 minutes of traffic\n   dimensions=timestamp&sites\n   top 100\n   output format csv")
            mycmd = ("curl -k -X GET 'https://localhost/cube/traffic.csv?slice=timestamp(-15minutes:now)&dimensions=timestamp,sites&measures=sum.total.bytes&api_key=" + firstSupportKey + "&a=top(auto,n:100)'")
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("-------------------------")
            print("In order to find the data view the system used we just need to modify our query to json and grep for view_name")
            mycmd = ("curl -k --silent -X GET 'https://localhost/cube/traffic.json?slice=timestamp(-15minutes:now)&dimensions=timestamp,sites&measures=sum.total.bytes&api_key=" + firstSupportKey + "&a=top(auto,n:100)' | json_pp | grep view_name")
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("----all done-------")
        elif(ch == 3):
            print ("Get a list of all dataviews via the data view API, write to a file (this is a big list, perhaps the next one is better)")
            mycmd = ("curl -k --silent -X GET 'https://localhost/api/data_views/?api_key=" + firstSupportKey + "' | json_pp | tee dataviewsdump.json") 
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("I've send the output to file dataviewsdump.json")
        elif(ch == 4):
            print("Dump a specific data view, selected from a menu of all configured data views")
            #url = 'https://localhost/dimension/router/positions?api_key=' + firstSupportKey
            url = 'https://localhost/api/data_views/?attributes=*&api_key=' + firstSupportKey
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
            mycmd = ("curl -k --silent -X GET 'https://localhost/api/data_views/" + dataviewuuid + "?api_key=" + firstSupportKey + "' | json_pp | tee mydataview.json") 
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("\n\nI've written the output to file mydataview.json for you")
        elif(ch == 5):
            print("Show me how to create a new data view")
            print("show the POST to the Devices Topology API to recreate it") 
            print ("If you then add/delete interfaces to the topology.json file they will change in the router")
            print("This one works around the missing GET in devices API")
            print("I am Building up the router model from several places")
            #start by listing all routers and askign the user to pick one 
            url = 'https://localhost/dimension/router/positions?attributes=*&api_key=' + firstSupportKey
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
            #find the router name and the possition
            index = 0
            for key in routerlist:
                index += 1
                if index == int(user_input):
                    routername = routerlist[key]['name']
                    routerpossition = routerlist[key]['position_id']
                    routerflowip = routerlist[key]['router']['flow_ip']
            #
            #get the router interfaces
            url = 'https://localhost/dimension/interfaces/positions?filter=(interface:router_pos_id,=,' + str(routerpossition) + ')&attributes=(*)&api_key=' + firstSupportKey
            routerinterfaces = requests.get(url, verify=False).json()
            #for debug the line below prints the json containing all of the router interfaces
            #print ("\nDebug url: " + url)
            #json_formatted_routerinterfaces = json.dumps(routerinterfaces, indent=2)
            #print ("\nDebug routerinterfaces: ", json_formatted_routerinterfaces)
            #
            #we have router name, routername
            #we have the router possition, routerpossition
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
            mycmd = ("curl --insecure -X POST -d '@topologyConfigFile.json' https://localhost/api/devices/topology?api_key=" + firstSupportKey)
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
        elif(ch == 6):
            print("Show me how to patch(modify) an existing data view")
        elif(ch == 7):
            print ("Show me how to PUT(replace) an existing data view")
        elif ch == 8:
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
    print("\tDeepfield Kafka")
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

# Main program  
topmenu() 



