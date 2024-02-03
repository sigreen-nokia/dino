import os
import sys
import json
import csv
import time
from pathlib import Path
#requests is a must have and is available with pip/pip3
try:
    import requests
except ImportError:
    print ("\nPlease Install python module requests using")
    print ("       'pip install requests'")
    print ("       or")
    print ("       'pip3 install requests'")
    print ("Then rerun\n")
    sys.exit(1)
#we install urllibs just to disable cert warnings
try:
    import urllib3
    urllib3.disable_warnings()
except ImportError:
    print ("\nPlease Install python module urlib3 using")
    print ("       'pip install urllib3'")
    print ("       or")
    print ("       'pip3 install urllib3'")
    print ("Then rerun\n")
    sys.exit(1)
#argparse is a must have and is available with pip/pip3
try:
    import argparse 
except ImportError:
    print ("\nPlease Install python module argparse using")
    print ("       'pip install argparse'")
    print ("       or")
    print ("       'pip3 install argparse'")
    print ("Then rerun\n")
    sys.exit(1)

#command line options handler
parser = argparse.ArgumentParser(description="log_dataview_size",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("fqdn", help="You Deepfleid cluster fqdn or ip adress")
parser.add_argument("api_key", help="Your Deepfield cluster users API key")
parser.add_argument("-log_dir", "--log_dir", action="store", default=".", help="The directory to store the log files, Example: /pipedream/log/")
args = parser.parse_args()
config = vars(args)
#print ("DEBUG: :config", config)
target_dir = Path(args.log_dir)
API_Key = args.api_key
cluster_fqdn =  args.fqdn

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

#print ("DEBUG: :target_dir", target_dir)
#print ("DEBUG: :API_Key", API_Key)
#print ("DEBUG: :cluster_fqdn", cluster_fqdn)

#constants
disk_space_filename=Path(str(target_dir) + "/data_view_disk_space.csv")
disk_space_filename_sorted=Path(str(target_dir) + "/data_view_disk_space_sorted.csv")
#print ("DEBUG: disk_space_filename:", disk_space_filename)
#print ("DEBUG: disk_space_filename_sorted:", disk_space_filename_sorted)

url = 'https://' + cluster_fqdn + '/api/data_views/?api_key=' + API_Key
#print ("DEBUG: url:", url)
#Main
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

