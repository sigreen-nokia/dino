import os
import sys
#import re
#import subprocess
#import socket
import json
import csv
import time
from pathlib import Path
#from subprocess import check_output as run
#from datetime import date
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

#functions to work out the fqdn and api key, prompt if this is not a dcu
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

API_Key = get_api_key()
cluster_fqdn = get_cluster_fqdn()

disk_space_filename=Path("data_view_disk_space.csv")
disk_space_filename_sorted=Path("data_view_disk_space_sorted.csv")
url = 'https://' + cluster_fqdn + '/api/data_views/?api_key=' + API_Key
dataviewlist = requests.get(url, verify=False).json()
json_formatted_dataviewlist = json.dumps(dataviewlist, indent=2)
#print ("DEBUG: json_formatted_dataviewlist:", json_formatted_dataviewlist)
py_formatted_dataviewlist = json.loads(json_formatted_dataviewlist)
#print ("DEBUG: py_formatted_dataviewlist:", py_formatted_dataviewlist)
dataviewmetadata = py_formatted_dataviewlist["metadata"]
#print ("\n\nDEBUG: dataviewmetadata", dataviewmetadata)
dataviewdata = py_formatted_dataviewlist["data"]
#print ("\n\nDEBUG: dataviewdata", dataviewdata)
#open the csv file to store the dataview disk sizes
#check if the file already exists
if disk_space_filename.is_file():
    file_exists = True
else: 
    file_exists = False
with open(disk_space_filename, 'a', newline='') as file:
    writer = csv.writer(file, delimiter=';', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
    #only add the top row is the file was just created
    if file_exists == False:
         writer.writerow(['dataview_name', 'epoc_time', 'size_on_disk']) 
    for key in py_formatted_dataviewlist["data"]:
         dataviewdata_name = key["name"]
         #print("DEBUG: dataviewdata_name {} ".format(dataviewdata_name))
         dataviewdata_timesteps = key["timesteps"]
         #print("DEBUG: dataviewdata_timesteps {} ".format(dataviewdata_timesteps))
         data_view_total_data_size_on_disk_bytes = 0
         for dataviewdata_timestep in key["timesteps"]:
              dataviewdata_timestep_data = dataviewdata_timesteps[dataviewdata_timestep]
              #print("DEBUG: dataviewdata_timestep_data {} ".format(dataviewdata_timestep_data))
              dataviewdata_timestep_data_size_on_disk_bytes = dataviewdata_timestep_data["size_on_disk_bytes"]
              #print("DEBUG: timestep\t{}\tdataviewdata_timestep_data_size_on_disk_bytes\t{}".format(dataviewdata_timestep,dataviewdata_timestep_data_size_on_disk_bytes))
              data_view_total_data_size_on_disk_bytes = data_view_total_data_size_on_disk_bytes + dataviewdata_timestep_data_size_on_disk_bytes
         #print("DEBUG: data_view_total_data_size_on_disk_bytes {}".format(data_view_total_data_size_on_disk_bytes))
         writer.writerow([dataviewdata_name,int(time.time()),data_view_total_data_size_on_disk_bytes]) 
#sort the file based on name, skipping the header
mycmd = ("cat " + str(disk_space_filename) + " | (sed -u 1q; sort) > " + str(disk_space_filename_sorted))
#print("DEBUG: Command is:" + mycmd )
os.system(mycmd)

