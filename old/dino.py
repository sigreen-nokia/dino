# importing the module
import os
import re
import subprocess
import deepy.cfg
import deepy.deepui
import get_context
import pandas as pd
import deepy.log as log
from subprocess import check_output as run

#statics
logDir = '/pipedream/log/'
uiLogName = 'ui.log'
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


def topmenu():

    os.system("clear")
    # sets the text color to white
    os.system("tput setaf 7")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDino - Deepfield customer engineer trainer")
    # sets the text color to white
    os.system("tput setaf 7")
    print("\t-------------------------------------------------")

    #incomming!!
    #swap
    #whats using my swap space
    #for file in /proc/*/status ; do awk '/VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; done | sort -k 2 -n -r 
    #how much swap do I have 
    #grep -i swap /proc/meminfo
    #mysql (<5.2)
    #mysql -u root -e "show databases";
    #mysql -u root -e "use defender_bt-tactical; show tables;"
    #mysql -u root -e "use defender_bt-tactical; describe Interfaces;"
    #postgres  (5.2+)
    #impala-shell
    #kafka
    #redis-cli keys "*license.json" | xargs redis-cli del
    #flow tracing
    #Check if we are receiving flow by router
    #flow.py --show-realtime
    #flow.py --show-realtime | grep worker02 | wc -l  
    #normd
    #pdvi.py traffic.json
    #bgp bgp.py --search 213.187.233.0/24
    #routemap.py -v show -a 213.187.233.0/24
    #dims.py dump interfaces -p 15630
    #flow.py --show-realtime | grep MLT1
    #diagnostics.py --skip-config --build-only -v
    #ptdump
    #python community.py 
    #dims.py dump suspicious | more
    #hdfs dfs -ls /pipedream/cache/dimensions/
    #mtr --no-dns --report --report-cycles 60 worker01
    #nodes with dnsflow sudo salt -G roles:dnsflow cmd.run 'supervisorctl status | grep dns'

    while True:
        print("""
            1.Whats a trainer ? 
            2.Deepfield Example Queries (empty) 
            3.Deepfield Cluster Health
            4.Deepfield Cluster Configuration 
            5.Queries the customer is using most frequently (view optimization, thanks ato)
            6.mysql (empty)
            7.postgres (empty)
            8.impala (empty)
            9.kafka (empty)
            10.redis (empty)
            11.tracing (empty)
            12.networking and bonding
            13.bgp (empty)
            14.Exit""")
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
            os.system("cal")
        elif ch == 8:
            os.system("systemctl status httpd")
        elif ch == 9:
            os.system("systemctl status docker")
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
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        topmenu()

def submenu22():
    os.system("clear")
    # sets the text color to white
    os.system("tput setaf 7")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Example Queries")
    # sets the text color to white
    os.system("tput setaf 7")
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
    # sets the text color to white
    os.system("tput setaf 7")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Cluster Health")
    # sets the text color to white
    os.system("tput setaf 7")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.salt-ping all nodes                      			#tests basic connectivity Master to each worker
            2.soup status on all nodes      		       		#checks the status of the Deepfield processes
            3.check disk space 						#show disk space available per partition for all nodes    
            4.memory hogs 						#show the top processes consuming memory for all nodes 
            5.cpu hogs 							#show the top processes consuming cpu for all nodes 
            6.show me the cpu details for each node 			#cpu details
            7.show me the cpu model for each node 			#cpu model
            8.get the cpu clock speeds for each node 			#wondering why one node is busy.. perhaps you have a fan out and the clock was stepped
            9.Return""")
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
            mycmd = "sudo salt \* cmd.run \"ps -eo %mem,%cpu,pid,ppid,cmd --sort=-%mem | cut -c -140 | head\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 5:
            mycmd = "sudo salt \* cmd.run \"ps -eo %mem,%cpu,pid,ppid,cmd --sort=-%cpu | cut -c -140 | head\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 6:
            mycmd = "sudo salt \* cmd.run \"lscpu\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 7:
            mycmd = "sudo salt \* cmd.run \"lshw | grep -i intel | grep -i cpu\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 8:
            mycmd = "sudo salt \* cmd.run \"cat /proc/cpuinfo | grep MHz\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 9:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu23()

def submenu24():
    os.system("clear")
    # sets the text color to white
    os.system("tput setaf 7")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Cluster Configuration")
    # sets the text color to white
    os.system("tput setaf 7")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.salt roles configured on each node 			#shows the configured services on each node 
            2.who has the dnsflow salt role     			#which dcu's
            3.who has the collector salt role     			#which dcu's
            4.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycmd = "sudo salt \* grains.get roles"
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 2):
            mycmd = "sudo salt -G roles:dnsflow test.ping"
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 3):
            mycmd = "sudo salt -G roles:collector test.ping"
            print("Command is:" + mycmd )
            os.system(mycmd)
        elif ch == 4:
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
    # sets the text color to white
    os.system("tput setaf 7")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Queries the customer is using most frequently (view optimization)")
    # sets the text color to white
    os.system("tput setaf 7")
    print("\t-------------------------------------------------")
    while True:
        print("""
            1.Show the most frequently ran customer queries in contexts traffic,backbone,big_cube 
            2.Show the most frequently ran customer queries in context subscriber
            3.Show the most frequently ran customer queries in context video_stream
            4.Show the most frequently ran customer queries in context flowdump
            5.Cleanup the /tmp/dino-* directories used to store the queries
            6.Return""")
        print("\n")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            mycontext = ['traffic', 'backbone', 'big_cube'] 
            getMostUsedQueries()
        elif ch == 2:
            mycontext = ['subscriber'] 
            getMostUsedQueries()
        elif ch == 3:
            mycontext = ['video_stream'] 
            getMostUsedQueries()
        elif ch == 4:
            mycontext = ['flowdump'] 
            getMostUsedQueries()
        elif ch == 5:
            os.system("rm -rf /tmp/dino-*")
        elif ch == 6:
            topmenu()
        else:
            print("Invalid entry")
        input("Press enter to continue")
        os.system("clear")
        submenu25()

def submenu212():
    os.system("clear")
    # sets the text color to white
    os.system("tput setaf 7")
    print("\n\t-------------------------------------------------")
    # sets the text colour to green
    os.system("tput setaf 2")
    print("\tDeepfield Networking")
    # sets the text color to white
    os.system("tput setaf 7")
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
        if(ch == 2):
            mycmd = "sudo salt \* cmd.run \"netstat -rn\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 3):
            mycmd = "sudo salt \* cmd.run \"cat /proc/net/bonding/bond0 | grep up\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 4):
            mycmd = "sudo salt \* cmd.run \"cat /proc/net/bonding/bond0\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 5):
            mycmd = "sudo salt \* cmd.run \"netstat -i\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 6):
            mycmd = "sudo salt \* cmd.run \"netstat -s\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 7):
            mycmd = "sudo salt \* cmd.run \"sudo netstat -tulpn | grep LISTEN\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 8):
            myport=input("Enter your port: ")
            mycmd = "sudo salt \* cmd.run \"sudo lsof -i:" + myport + "\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 9):
            mycmd = "sudo salt \* cmd.run \"ntpq -p\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 10):
            mycmd = "sudo salt \* cmd.run \"date\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 11):
            mycmd = "sudo salt \* cmd.run \"nc -zv genome.deepfield.net 443\""
            print("Command is:" + mycmd )
            os.system(mycmd)
        if(ch == 12):
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



def whatsatrainer():
     print("""
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
    print("	/tmp/dino-" + str(os.getpid()) + "/querysummary_sorted_on_count.csv contains the queries sorted on number of hits")
    print("	/tmp/dino-" + str(os.getpid()) + "/queries_from_logs.txt contains the log entries for all querys found")
    print("\n\nSome of the files can get quite large, so if you do not planning to use them you might consider cleanig up with \n")
    print("rm -rf /tmp/dino-" + str(os.getpid()))


def makeTempDir():
    tmpDirPath = ('/tmp/dino-' + str(os.getpid()))  
    log.info('Creating dir ' + str(tmpDirPath))
    os.mkdir(str(tmpDirPath))
    os.chdir(tmpDirPath)

# Main program  
topmenu() 



