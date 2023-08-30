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
            19.Defender (DDoS)
            20.Dimensions
            21.Exit""")
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
            submenu219() 
        elif ch == 20:
            submenu220() 
        elif ch == 21:
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

def submenu219():
    os.system("clear")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDefender (DDoS)")
    # sets the text color to magenta
    os.system("tput setaf 6")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Build up a def.py report, to gather up the defender configuration and running details
            2.Detection: Whats my current running Defender mitigation branch
            3.Detection: Get a list of all available secure genome mitigation versions
            4.Mitigation: Whats my current running Defender mitigation branch
            5.Mitigation: Get a list of all available secure genome mitigation versions
            6.Create a custom protection group with ipv4 subnets covering the internet.
            7.Return""")
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
            print ("Grabbing your clusters current Secure Genome Detection rule set branch")
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
            mycmd = ("curl --insecure -X GET https://localhost/api/secure_genome/version/detection?api_key=" + firstSupportKey + " | json_pp" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
        elif(ch == 3):
            print ("Getting a list of all available secure genome versions")
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
            mycmd = ("curl --insecure -X GET https://localhost/api/secure_genome/versions/detection?api_key=" + firstSupportKey + " | json_pp" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
        elif(ch == 4):
            print ("Grabbing your clusters current Secure Genome Mitigation rule branch")
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
            mycmd = ("curl --insecure -X GET https://localhost/api/secure_genome/version/mitigation?api_key=" + firstSupportKey + " | json_pp" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
        elif(ch == 5):
            print ("Getting a list of all available secure genome Mitigation rule set versions")
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
            mycmd = ("curl --insecure -X GET https://localhost/api/secure_genome/versions/mitigation?api_key=" + firstSupportKey + " | json_pp" )
            print("\nCommand is:" + mycmd )
            os.system(mycmd)
        elif ch == 6:
            print("\n Look in the Dimensions menu for this one.")
        elif ch == 7:
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
            5.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
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
        if(ch == 1):
            print("Dump a specific dimension, selected from a menu of all configured dimensions")
            url = 'https://localhost/dimensions/index?attributes=*&api_key=' + firstSupportKey
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
            mycmd = ("curl -k --silent -X GET 'https://localhost/dimension/" + str(dimensionuuid) + "?api_key=" + firstSupportKey + "' | json_pp | tee mydimension.json") 
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("\n\nI've written the output to file mydimension.json for you")
        elif(ch == 2):
            print("Create a new dimension from a json file - A step by step")
            dimension_filename = input("enter the json filename to import the dimension from:")
            DimensionName=input("Enter a name for your new custom dimension: ")
            print("\n\nThe following command will add the JSON in order to create a new data view")
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@" + dimension_filename + "' https://localhost/dimension/" + DimensionName + "?api_key=" + firstSupportKey)
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
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@custom-dimension-example.json' https://localhost/dimension/" + DimensionName + "?api_key=" + firstSupportKey)
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will create the dimension for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
                ###########
                print("Now lets add the possitions containing the subnets\n")
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
                print ("\n\nWe will use the Deepscript endpoint to read our csv file and turn it into possitions.")
                print ("\nThe following command will create the possitions in our custom dimension")
                mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' --data-binary '@subnet-example.csv' https://localhost/deepscript/dimension/" + DimensionName + "?api_key=" + firstSupportKey)
                print("Command is:" + mycmd )
                user_input = input("Input yes and I will create the possitions for you, any other key to do nothing at all:")
                if user_input == 'yes':
                    print("\nRunning Command: " + mycmd )
                    os.system(mycmd)
                    print("\nDone")
        elif(ch == 4):
            print("Delete a specific dimension, selected from a menu of all configured dimensions")
            url = 'https://localhost/dimensions/index?attributes=*&api_key=' + firstSupportKey
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
            mycmd = ("curl -k --silent -X DELETE 'https://localhost/dimension/" + str(dimensionuuid) + "?api_key=" + firstSupportKey + "' | json_pp ") 
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will delete the dimension for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\n\nAll Done")
        elif ch == 5:
            topmenu()
        else:
            print("Invalid entry")
        input("\nPress enter to continue")
        os.system("clear")
        submenu220()

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
            13.dump /etc/network/interfaces for all nodes
            14.Return""")
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
            mycmd = "sudo salt \* cmd.run \"cat /etc/network/interfaces\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 14:
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
            8.Set a single specified routers interface to 'active' true/false
            9.count 'active' for all interfaces on a specified router
            10.Set all interfaces on a specified router to 'active' true/false (receiving flow)
            11.count 'active' for all interfaces on all routers
            12.Set all interfaces 'active' true/false on all routers
            13.Overwrite a specified routers interface name, intended for config rules (works but then gets reset to router name + ifname )
            14.Debugging hints
            15.Return""")
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
            print ("Set a single routers interface to active true/false (receiving flow)")
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
            print ("The interface can have three settings t/f/[blank]\nwhich means true false or no 'active' parameter present\nThe current setting for active is\n")
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active from \"Interfaces\" where id=" + str(interfacepossitionselected) + " order by id;'")
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
        elif(ch == 9):
            print ("Count the 'active' settings t/f/[blank] on all interfaces of a specified router")
            #first get a router from the list
            #start by listing all routers and ask the user to pick one 
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

            #count the existing interfaces t/f/[blank]
            print ("Counting the t/f/[blank] interfaces for the router ", routername)
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active, COUNT(*) from \"Interfaces\" where _interface_router_pos_id=" + str(routerpossition) + " group by active;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )

        elif(ch == 10):
            print ("Set all interfaces on a specified router to active true/false (receiving flow)")
            #first get a router from the list
            #start by listing all routers and ask the user to pick one 
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
            #count the existing interfaces t/f/[blank]
            print ("Counting the t/f/[blank] interfaces for the router ", routername)
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active, COUNT(*) from \"Interfaces\" where _interface_router_pos_id=" + str(routerpossition) + " group by active;'")
            os.system(mycmd)
            print("\nI used this Command: " + mycmd )
            print("\nHow do you want me to set active)")
            print("\nHow do you want me to set the active parameter for all of router" + routername + " interfaces)")
            user_input = input("Input true or false any other key makes no change:")
            if user_input == 'true':
                print ("setting to active=true for all interfaces on router " + routername + ". I used this comand")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'update \"Interfaces\" set active='true' where _interface_router_pos_id=" + str(routerpossition) + ";'")
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            elif user_input == 'false':
                print ("setting to active=false for all interfaces on router " +routername + ". I used this comand")
                mycmd = ("sudo -u postgres psql -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'update \"Interfaces\" set active='false' where _interface_router_pos_id=" + str(routerpossition) + ";'") 
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing")
            #recount the existing interfaces t/f/[blank]
            print ("Re-counting the t/f/[blank] interfaces for the router ", routername)
            mycmd = ("sudo -u postgres psql -t -d \"defender_" + socket.gethostname().split('.', 2)[1] + "\" -c 'select active, COUNT(*) from \"Interfaces\" where _interface_router_pos_id=" + str(routerpossition) + " group by active;'")
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
            5.Starhub Example Case:Create a new custom ddos data view for regs (high retention) - A step by step using an example
            6.LGU+ Example Case: Create a new custom ddos data view sliced on a custom protection group - A step by step using an example
            7.Create a new data view from a json file - A step by step
            8.Patch an existing data view retention - A step by step
            9.Delete an existing data view
            10.Return""")
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
            print("Hint: For very long query results json_pp can hang, in which case use jq . instead")
            mycmd = ("curl -k --silent -X GET 'https://localhost/cube/traffic.json?slice=timestamp(-15minutes:now)&dimensions=timestamp,sites&measures=sum.total.bytes&api_key=" + firstSupportKey + "&a=top(auto,n:100)' | json_pp | grep view_name")
            print("Command is:" + mycmd )
            input("Press any key and I'll run the command...")
            os.system(mycmd)
            print("----all done-------")
        elif(ch == 3):
            print ("Get a list of all data views via the data view API, write to a file (this is a big list, perhaps the next one is better)")
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
            print("Starhub example case: Create a new custom ddos data view for regs (long retention) - A step by step")
            url = 'https://localhost/api/data_views/?attributes=*&api_key=' + firstSupportKey
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
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@ddos-baseline-example.json' https://localhost/api/data_views/?api_key=" + firstSupportKey)
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
            print("LGU+ example case: Create a new custom ddos data view sliced on a custom protection group - A step by step")
            url = 'https://localhost/api/data_views/?attributes=*&api_key=' + firstSupportKey
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
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@ddos-baseline-example.json' https://localhost/api/data_views/?api_key=" + firstSupportKey)
            print("Command is:" + mycmd )
            user_input = input("Input yes and I will create the dataview for you, any other key to do nothing at all:")
            if user_input == 'yes':
            #if(len(user_input) != 0):
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\n\nGive it an hour and the following example query should hit your new dataview")
                print("\ncurl -k --silent -X GET 'https://localhost/cube/traffic.json?slice=timestamp(-60minutes:now)&dimensions=timestamp,ddos,origin_asn.src,protocol,tcpflags,category,country.src,addr.src,addr.dst,port.src,port.dst&measures=avg.bps,pctl95.bps,percent_total(sum.bytes)&apply=sort(timestamp,asc)&apply=top(all,n:100)&apply=timestep(5min,5min)&bs=((boundary.peering.input,true))&slice:or=(ExampleCustomProtectedObject.dst!(None))&slice:or=(category(12))&api_key=31UO2fiKwinzYl' | jq . | grep view_name")
                print("\nAll Done")
            else:
                print ("doing nothing. You can use the curl above to create the dataview yourself")
        elif(ch == 7):
            print("Create a new dataview from a json file - A step by step")
            print("hint1: build data views with 10s and 2min timesteps with a source_timestep of 10s")
            print("hint2: build data views with 30min, 2hr and day timesteps from a parent view with a 5min timestamp and the same dimensions, base_view for example. you cannot use 10s")
            data_view_filename = input("enter the json filename to import the data view from:")
            print("\n\nThe following command will add the JSON in order to create a new data view")
            mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@" + data_view_filename + "' https://localhost/api/data_views/?api_key=" + firstSupportKey)
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
            url = 'https://localhost/api/data_views/?attributes=*&api_key=' + firstSupportKey
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
            mycmd = ("curl -k --silent -X GET 'https://localhost/api/data_views/" + dataviewuuid + "?api_key=" + firstSupportKey + "' | json_pp | tee example_dataview.json") 
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
            mycmd = ("curl --insecure -X PATCH -H 'Content-Type: application/json' -d '@patch-data-view.json' https://localhost/api/data_views/?api_key=" + firstSupportKey)
            print("\nCommand is:" + mycmd )
            user_input = input("\nInput yes and I will create the data view for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing. You can use the curl above to create the data view yourself")
        elif(ch == 9):
            print ("Delete an existing data view")
            url = 'https://localhost/api/data_views/?attributes=*&api_key=' + firstSupportKey
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
            #mycmd = ("curl --insecure -X POST -H 'Content-Type: application/json' -d '@example_dataview.json' https://localhost/api/data_views/?api_key=" + firstSupportKey)
            mycmd = ("curl -k --silent -X DELETE 'https://localhost/api/data_views/" + dataviewuuid + "?api_key=" + firstSupportKey + "' ")
            print("Command is:" + mycmd )
            user_input = input("WARNING: Input yes and I will delete the data view for you, any other key to do nothing at all:")
            if user_input == 'yes':
                print("\nRunning Command: " + mycmd )
                os.system(mycmd)
                print("\nDone")
            else:
                print ("doing nothing. You can use the curl above to delete the data view yourself")
        elif ch == 10:
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



