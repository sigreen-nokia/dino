# importing the modules
#To add missing modues: 
#                       pip install [module name]: 
#                       or 
#                       pip3 install [module name]: 
import os
import sys 
import re
import subprocess
from subprocess import check_output as run

def get_dynamic_interface_ips_ip(interface):
    #Get IP addresses for a given network interface from ip addr show
    command = f"ip addr show {interface}"
    output = subprocess.check_output(command, shell=True).decode()
    #print ("DEBUG: get_dynamic_interface_ips_ifconfig: output:", output)
    ip_pattern = r'inet\s+(\d+\.\d+\.\d+\.\d+)'
    match = re.findall(ip_pattern, output)
    if match:
        match = sorted(match)
        #print ("DEBUG: get_dynamic_interface_ips_ifconfig: match:", match)
        return match 
    else:
        return None

def get_dynamic_interface_ips_ifconfig(interface):
    #Get IP addresses for a given network interface from ifconfig
    command = f"ifconfig {interface}"
    output = subprocess.check_output(command, shell=True).decode()
    #print ("DEBUG: get_dynamic_interface_ips_ifconfig: output:", output)
    #we are dealing with different versions of ofconfig output here inet vs inet addr:
    ip_pattern = r'inet addr:+(\d+\.\d+\.\d+\.\d+)'
    match = re.findall(ip_pattern, output)
    if match:
        match = sorted(match)
        #print ("DEBUG: get_dynamic_interface_ips_ifconfig: match:", match)
        return match
    else:
        ip_pattern = r'inet +(\d+\.\d+\.\d+\.\d+)'
        match = re.findall(ip_pattern, output)
        if match:
            match = sorted(match)
            #print ("DEBUG: get_dynamic_interface_ips_ifconfig: match:", match)
            return match
        else:
            return None

def get_dynamic_interface_name_list_ip():
    #Get a list of all ip links interface name from ip addr shows
    result = "" 
    command = f"ip link show | grep \"^[0-9]\" | cut -d\" \" -f2 | sed \"s/://\" | sed \"s/@.*//\""
    output = subprocess.check_output(command, shell=True).decode()
    #remove blank lines
    output = os.linesep.join([s for s in output.splitlines() if s])
    #print ("DEBUG: interface_name_list output:", output)
    if output:
        InterfaceList = list(output.split("\n"))
        # remove empty entries in the list
        InterfaceList = list(filter(None, InterfaceList))
        InterfaceList = sorted(InterfaceList)
        #print ("DEBUG: interface_name_list InterfaceList:", InterfaceList)
        return InterfaceList 
    else:
        print ("ERROR: no ip link show interfaces found")
        return None

def get_dynamic_interface_name_list_ifconfig():
    #Get a list of all ip links interface names from ifconfig
    result = "" 
    command = f"ifconfig | grep -e \"Link\" -e \"flags=\" | cut -d\" \" -f1 | sed \"/^$/d\" | sed \"s/:$//\""
    output = subprocess.check_output(command, shell=True).decode()
    #remove blank lines
    output = os.linesep.join([s for s in output.splitlines() if s])
    #print ("DEBUG: interface_name_list output:", output)
    if output:
        IfconfigInterfaceList = list(output.split("\n"))
        # remove empty entries in the list
        IfconfigInterfaceList = list(filter(None, IfconfigInterfaceList))
        IfconfigInterfaceList = sorted(IfconfigInterfaceList)
        #remove any occurance of the loopback lo as in some OS the loopback ip is not printed dynamicaly
        IfconfigInterfaceList = remove_list_string(IfconfigInterfaceList, "lo")
        #print ("DEBUG: interface_name_list IfconfigInterfaceList:", IfconfigInterfaceList)
        return IfconfigInterfaceList 
    else:
        print ("ERROR: no ifconfig interfaces found")
        return None
#here
def get_dynamic_static_routes():
    command = f"ip route show | grep via"
    output = subprocess.check_output(command, shell=True).decode()
    #print ("DEBUG: get_dynamic_static_routes: output:\n", output)
    output = os.linesep.join([s for s in output.splitlines() if s])
    if output:
        DynamicStaticRoutes  = list(output.split("\n"))
        # remove empty entries in the list
        DynamicStaticroutes = list(filter(None, DynamicStaticRoutes))
        DynamicStaticRoutes = sorted(DynamicStaticRoutes)
        #print ("DEBUG: get_dynamic_static_routes: DynamicStaticRoutes:\n", DynamicStaticRoutes)
        return DynamicStaticRoutes 
    else:
        return None

def get_static_static_routes():
    command = f"cat /etc/network/interfaces /etc/network/interfaces.d/* | grep -e \"route add\" -e \"gateway\""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        #print ("DEBUG: get_static_static_routes: output:\n", output)
        output = os.linesep.join([s for s in output.splitlines() if s])
    except subprocess.CalledProcessError as e:
        print ("WARNING: No interfaces files found in /etc/networks/*")
        output = []
    # 'No such file or directory' doesn't return a non zero exit, so no exception, we have to handle it seperately.
    # one ocurance of 'No such file..' is fine, as we are testing for files in two directories and may have found them in one 
    # two or more ocurances means we didn't find any static network config file in /etc/networks/
    tmp_count = str(output).count('No such file or directory')
    #print ("DEBUG: get_static_static_routes: tmp_count:", tmp_count)
    if tmp_count > 1:
        #print ("DEBUG: get_static_static_routes: output:", output)
        return None 
    if output:
        StaticStaticRoutes  = list(output.split("\n"))
        # remove empty entries in the list
        StaticStaticRoutes = list(filter(None, StaticStaticRoutes))
        StaticStaticRoutes = sorted(StaticStaticRoutes)
        #remove any occurance of 'No such file or directory' so its  not treated as an interface name
        StaticStaticRoutes = remove_list_string(StaticStaticRoutes, "No such file or directory")
        #print ("DEBUG: get_static_static_routes: StaticStaticRoutes:\n", StaticStaticRoutes)
        return StaticStaticRoutes 
    else:
        return output 


def get_static_interface_name_list():
    #Get a list of all interfaces files interface names
    result = ""
    command = f"cat /etc/network/interfaces /etc/network/interfaces.d/* | grep \"^auto\|^allow-hotplug\" | cut -d\" \" -f2"
    try:
        #stderr=subprocess.STDOUT is to redirects error No such file or directory
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        #print ("DEBUG: static_interface_name_list_1 output:", output)
        #remove blank lines
        output = os.linesep.join([s for s in output.splitlines() if s])
        #print ("DEBUG: static_interface_name_list_2 output:", output)
    except subprocess.CalledProcessError as e:
        #print ("DEBUG: static_interface_name_list_3 output:", output)
        print ("WARNING: No interfaces files found in /etc/networks/*")
        output = [] 
    # 'No such file or directory' doesn't return a non zero exit, so no exception, we have to handle it seperately.
    # one ocurance of 'No such file..' is fine, as we are testing for files in two directories and may have found them in one 
    # two or more ocurances means we didn't find any static network config file in /etc/networks/
    tmp_count = str(output).count('No such file or directory')
    #print ("DEBUG: get_static_interface_name_list_4:", tmp_count)
    if tmp_count > 1:
        #print ("DEBUG: static_interface_name_list_5 output:", output)
        return None 
    if output:
        #create a list
        InterfaceList = list(output.split("\n"))
        # remove empty entries in the list
        InterfaceList = list(filter(None, InterfaceList))
        InterfaceList = sorted(InterfaceList)
        #remove any occurance of 'No such file or directory' so its  not treated as an interface name
        InterfaceList = remove_list_string(InterfaceList, "No such file or directory")
        #remove any occurance of the loopback lo as in some OS the loopback ip is not printed dynamicaly
        InterfaceList = remove_list_string(InterfaceList, "lo")
        #print ("DEBUG: static_interface_name_list_6 InterfaceList:", InterfaceList)
        return InterfaceList
    else:
        #print ("DEBUG: static_interface_name_list_7 InterfaceList:", InterfaceList)
        print ("WARNING: no /etc/networks/* files found, so I cannot extract the interface names")
        return None

def diff_list2_list1(list1,list2):
    #diff two lists
    #print ("DEBUG: diff_list2_list1_1: list1:", list1)
    #print ("DEBUG: diff_list2_list1_1: list2:", list2)
    #remove any occurance of '127.0.0.1' 
    #As the local interface gets given a loopback ip address in ifconfig, 
    #but static config sometimes says lo without any ip address, 
    #so we should omit 127.0.0.1 as a difference to avoid firing a fase possitive
    #list1 = remove_list_string(list1, "127.0.0.1")
    #list2 = remove_list_string(list2, "127.0.0.1")
    ListDiff = []
    for element in list2 or []:
        if element not in list1:
            #print ("DEBUG: diff_list2_list1_2: element:", element)
            #the local interface gets given a loopback ip address in ifconfig, 
            #but static config says lo without any ip address, 
            #so we should omit 127.0.0.1 as a difference to avoid firing a fase possitive
            #if element == ['127.0.0.1']:
            #     element = [''] 
            #print ("DEBUG: diff_list2_list1_3: element:", element)
            ListDiff.append(element)
    #print ("DEBUG: diff_list2_list1_4: ListDiff:", ListDiff)
    return(ListDiff)

def diff_list1_list2(list1,list2):
    #diff two lists
    #print ("DEBUG: diff_list1_list2_1: list1:", list1)
    #print ("DEBUG: diff_list1_list2_1: list2:", list2)
    ListDiff = []
    for element in list1 or []:
        if element not in list2:
            #the local interface gets given a loopback ip address in ifconfig, 
            #but static config says lo without any ip address, 
            #so we should omit 127.0.0.1 as a difference to avoid firing a fase possitive
            if element == ['127.0.0.1']:
                 element = [''] 
            ListDiff.append(element)
    #print ("DEBUG: diff_list1_list2_2: ListDiff:", ListDiff)
    return(ListDiff)

def get_static_interface_ip(interface):
    #Get IP addresses for a given network interface from static config
    #here we look for iface {interface name} then grab the block up to the next empoty line or end of file
    command = f"cat /etc/network/interfaces /etc/network/interfaces.d/* | sed -n '/iface {interface} /,/^$/p'"
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        #print ("DEBUG: get_static_interface_ip output:", output)
        ip_pattern = r'address\s+(\d+\.\d+\.\d+\.\d+)'
        match = re.findall(ip_pattern, output)
    except subprocess.CalledProcessError as e:
        print ("WARNING: No interfaces files found in /etc/networks/*")
        match = []
    # 'No such file or directory' doesn't return a non zero exit, so no exception, we have to handle it seperately.
    # one ocurance of 'No such file..' is fine, as we are testing for files in two directories and may have found them in one 
    # two or more ocurances means we didn't find any static network config file in /etc/networks/
    tmp_count = str(match).count('No such file or directory')
    #print ("DEBUG: get_static_interface_ip: :", match)
    if tmp_count > 1:
        #print ("DEBUG: get_static_interface_ip: match:", match)
        return None 
    if match:
        match = sorted(match)
        #remove any occurance of 'No such file or directory' so its  not treated as an interface name
        match = remove_list_string(match, "No such file or directory")
        #print ("DEBUG: get_static_interface_ip match:", match)
        return match
    else:
        return None

def get_static_interface_ip_list():
     #makes a sorted list of interface ip addresses for all interfaces fron static config
     static_ip_addresses = []
     for Static_InterfaceName in get_static_interface_name_list() or []:
         #print ("DEBUG: get_static_interface_ip_list_1: Static_InterfaceName:", Static_InterfaceName)
         my_static_ip_addresses=get_static_interface_ip(Static_InterfaceName)
         #for interfaces with no ip address we get a return None, convert to a list format
         if my_static_ip_addresses is None:
             my_static_ip_addresses = ['']
         static_ip_addresses.append(my_static_ip_addresses)
     if static_ip_addresses:
         #print ("DEBUG: get_static_interface_ip_list: static_ip_addresses:", static_ip_addresses)
         static_ip_addresses = sorted(static_ip_addresses)
         #print ("DEBUG: get_static_interface_ip_list: static_ip_addresses sorted:", static_ip_addresses)
         return static_ip_addresses
     else:
          return None 

def get_dynamic_interface_ip_list():
     #makes a sorted list of interface ip addresses for all interfaces fron dynamic config
     dynamic_ip_addresses = []
     for Dynamic_InterfaceName in get_dynamic_interface_name_list_ifconfig() or []:
         my_dynamic_ip_addresses=get_dynamic_interface_ips_ifconfig(Dynamic_InterfaceName)
         #print ("DEBUG: get_dynamic_interface_ip_list_1: Dynamic_InterfaceName:", Dynamic_InterfaceName)
         #print ("DEBUG: get_dynamic_interface_ip_list_1: my_dynamic_ip_addresses=get_dynamic_interface_ips_ifconfig:", my_dynamic_ip_addresses)
         #for interfaces with no ip address we get a return None, convert to a list format
         if my_dynamic_ip_addresses is None:
             my_dynamic_ip_addresses = ['']
         #moved this check to the diff functions
         #the local interface gets given a loopback ip address in ifconfig, but static config says lo without any ip address, 
         ##so we should omit this one as a difference to avoid firing a fase possitive
         #if my_dynamic_ip_addresses == ['127.0.0.1']:
         #    my_dynamic_ip_addresses = [''] 
         dynamic_ip_addresses.append(my_dynamic_ip_addresses)
     if dynamic_ip_addresses:
         #print ("DEBUG: get_dynamic_interface_ip_list: dynamic_ip_addresses:", dynamic_ip_addresses)
         dynamic_ip_addresses = sorted(dynamic_ip_addresses)
         #print ("DEBUG: get_dynamic_interface_ip_list: dynamic_ip_addresses sorted:", dynamic_ip_addresses)
         return dynamic_ip_addresses
     else:
         return None 


def check_static_route_post_up():
    command = f"cat /etc/network/interfaces /etc/network/interfaces.d/* | grep \"up route\" | grep -v \"post-up route\""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        output= list(output.split("\n"))
        # remove empty entries in the list
        output = list(filter(None, output))
        output = sorted(output)
        #print ("DEBUG: check_static_route_post_up:", output)
    except subprocess.CalledProcessError as e:
        print ("WARNING: No interfaces files found in /etc/networks/*")
        output = []
    # 'No such file or directory' doesn't return a non zero exit, so no exception, we have to handle it seperately.
    # one ocurance of 'No such file..' is fine, as we are testing for files in two directories and may have found them in one
    # two or more ocurances means we didn't find any static network config file in /etc/networks/
    tmp_count = str(output).count('No such file or directory')
    #print ("DEBUG: check_static_route_post_up: tmp_count:", tmp_count)
    if tmp_count > 1:
        #print ("DEBUG: static_interface_name_list_4 output:", output)
        return None
    if output:
        #remove any occurance of 'No such file or directory' so its  not treated as an interface name
        output = remove_list_string(output, "No such file or directory")
        #print ("DEBUG: check_static_route_post_up output:", output)
        return output 
    else:
        return None 

def check_static_route_add():
    command = f"cat /etc/network/interfaces /etc/network/interfaces.d/* | grep \"route add\" | grep -v \"ip route add\""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        output= list(output.split("\n"))
        # remove empty entries in the list
        output = list(filter(None, output))
        output = sorted(output)
        #print ("DEBUG: check_static_route_route_add:", output)
    except subprocess.CalledProcessError as e:
        print ("WARNING: No interfaces files found in /etc/networks/*")
        output = []
    # 'No such file or directory' doesn't return a non zero exit, so no exception, we have to handle it seperately.
    # one ocurance of 'No such file..' is fine, as we are testing for files in two directories and may have found them in one 
    # two or more ocurances means we didn't find any static network config file in /etc/networks/
    tmp_count = str(output).count('No such file or directory')
    #print ("DEBUG: check_static_route_add: tmp_count:", tmp_count)
    if tmp_count > 1:
        #print ("DEBUG: check_static_route_add: output:", output)
        return None 
    if output:
        #remove any occurance of 'No such file or directory' so its  not treated as an interface name
        output = remove_list_string(output, "No such file or directory")
        #print ("DEBUG: check_static_route_add: output:", output)
        return output 
    else:
        return None 

def check_static_mtu():
    command = f"cat /etc/network/interfaces /etc/network/interfaces.d/* | grep \"mtu\""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        #print ("DEBUG: check_static_mtu_1: output:", output)
        output= list(output.split("\n"))
        #remove empty entries in the list
        output = list(filter(None, output))
        output = sorted(output)
        #print ("DEBUG: check_static_mtu_2: output:", output)
    except subprocess.CalledProcessError as e:
        #print ("DEBUG: check_static_mtu_3: output:", output)
        print ("WARNING: No interfaces files found in /etc/networks/*")
        return None 
    # 'No such file or directory' doesn't return a non zero exit, so no exception, we have to handle it seperately.
    # one ocurance of 'No such file..' is fine, as we are testing for files in two directories and may have found them in one 
    # two or more ocurances means we didn't find any static network config file in /etc/networks/
    tmp_count = str(output).count('No such file or directory')
    #print ("DEBUG: check_static_mtu_4: tmp_count:", tmp_count)
    #print ("DEBUG: check_static_mtu_4: output:", output)
    if tmp_count > 1:
        #print ("DEBUG: static_interface_name_list_5 output:", output)
        return None 
    if output:
        #remove any occurance of 'No such file or directory' so its  not treated as an interface name
        output = remove_list_string(output, "No such file or directory")
        #print ("DEBUG: static_interface_name_list_6 output:", output)
        return output 
    else:
        return None 

def remove_list_string(my_list, my_string):
    #print ("DEBUG: remove_list_string: my_string:", my_string)
    #print ("DEBUG: remove_list_string: my_list:", my_list)
    res = []
    for sub in my_list:
        flag = 0
        if my_string in sub:
            flag = 1
        if not flag:
            res.append(sub)
    #print ("DEBUG: remove_list_string: res:", res)
    return res


# Main program  
print ("====================================================")
print ("Sumarising the running dynamic network configuration")
print ("====================================================")
ip_interface_names_ifconfig = get_dynamic_interface_name_list_ifconfig()
if ip_interface_names_ifconfig:
    print(f"ifconfig Interface Names: {ip_interface_names_ifconfig}")
else:
    print(f"No ifconfig Interface Names")
if get_dynamic_interface_name_list_ifconfig() == None:
        print(f"No interface names were found in /etc/networks/*")
else:
    for InterfaceName in get_dynamic_interface_name_list_ifconfig() or []:
        ip_addresses = get_dynamic_interface_ips_ifconfig(InterfaceName)
        if ip_addresses:
            print(f"IP addresses of {InterfaceName}: {ip_addresses}")
        else:
            print(f"No IP address found for {InterfaceName}")
dynamic_static_routes = get_dynamic_static_routes()
if dynamic_static_routes:
    print(f"Dynamically configured Static Routes: {dynamic_static_routes}")
else:
    print(f"No Dynamic Static Routes")

print ("==========================================================")
print ("Sumarising the static network configuration /etc/network/*")
print ("==========================================================")
static_ip_interface_names = get_static_interface_name_list()
if static_ip_interface_names:
    print(f"Static IP Interface Names: {static_ip_interface_names}")
else:
    print(f"No IP Interface names are configured in /etc/networks/*")
if get_static_interface_name_list() == None:
        print(f"No IP address were found in /etc/networks/*")
else:
    for Static_InterfaceName in get_static_interface_name_list() or []:
        static_ip_addresses = get_static_interface_ip(Static_InterfaceName)
        if static_ip_addresses:
            print(f"IP addresses of {Static_InterfaceName}: {static_ip_addresses}")
        else:
            print(f"No IP address found for {Static_InterfaceName} in /etc/networks/*")
static_static_routes = get_static_static_routes()
if static_static_routes:
    print(f"Statically configured Static Routes found in /etc/networks/*: {static_static_routes}")
else:
    print(f"No statically configured Static Routes found in /etc/networks/*")

print ("====================================================================================")
print ("Checking for interface name differences between the static and dynamic configuration")
print ("====================================================================================")
print ("####Checking for dynamic interfaces that are missing in static config###")
if get_static_interface_name_list() == None and get_dynamic_interface_name_list_ifconfig() == None:
        print(f"No static or dynamic network config were found to diff")
elif get_static_interface_name_list() == None:
        print(f"No static network configuration was found in /etc/networks/*")
        print(f"Your dynamic network interface names are listed below")
        print(f"Dynamic configuration Interface Names: {get_dynamic_interface_name_list_ifconfig()}")
elif get_dynamic_interface_name_list_ifconfig() == None: 
        print(f"No dynamic network configuration was found")
        print(f"Your static network configuration interface names are listed below")
        print(f"Static network configuration Interface Names: {get_static_interface_name_list()}")
else:
    interface_name_differences = diff_list2_list1(get_static_interface_name_list(),get_dynamic_interface_name_list_ifconfig())
    if interface_name_differences:
        print(f"CRITICAL: The following interface names are present in ifconfig")
        print(f"CRITICAL: However are missing in your static config /etc/network/interfaces or /etc/network/interfaces.d/*:")
        print(f"CRITICAL:{interface_name_differences}")
        print(f"CRITICAL: If you restart the node you will most likely loose these interfaces")
    else:
        print(f"No interface name differences were found between ifconfig and /etc/network/*")
print ("####Checking for static config that is missing in the dynamic interfaces####")
if get_static_interface_name_list() == None and get_dynamic_interface_name_list_ifconfig() == None:
        print(f"No static or dynamic network config were found to diff")
elif get_static_interface_name_list() == None:
        print(f"No static network configuration was found in /etc/networks/*")
        print(f"Your dynamic network interface names are listed below")
        print(f"Dynamic configuration Interface Names: {get_dynamic_interface_name_list_ifconfig()}")
elif get_dynamic_interface_name_list_ifconfig() == None: 
        print(f"No dynamic network configuration was found")
        print(f"Your static network configuration interface names are listed below")
        print(f"Static network configuration Interface Names: {get_static_interface_name_list()}")
else:
    interface_name_differences = diff_list1_list2(get_static_interface_name_list(),get_dynamic_interface_name_list_ifconfig())
    if interface_name_differences:
        print(f"CRITICAL: The following interface names are present in static config /etc/network/interfaces or /etc/network/interfaces.d/*")
        print(f"CRITICAL: However are missing in ifconfig")
        print(f"CRITICAL:{interface_name_differences}")
        print(f"CRITICAL: If you restart these new static interfaces may appear and cause a problem")
    else:
        print(f"No interface name differences were found between /etc/network/* and ifconfig")

print ("==========================================================================================")
print ("Checking for interface ip address differences between the static and dynamic configuration")
print ("==========================================================================================")
print ("####Checking for dynamic interfaces that are missing in static config####")
if get_static_interface_ip_list() == None and get_dynamic_interface_ip_list() == None:
        print(f"No static or dynamic network ip addresses were found to diff")
elif get_static_interface_ip_list() == None:
        print(f"No static network configuration ip addresses were found in /etc/networks/*")
        print(f"Your dynamic network interface ip addresses are listed below")
        print(f"Dynamic network IP addresses: {get_dynamic_interface_ip_list()}")
elif get_dynamic_interface_ip_list() == None: 
        print(f"No dynamic network configuration ip addresses were found")
        print(f"Your static network configuration interface names are listed below")
        print(f"Static network IP addresses: {get_static_interface_ip_list()}")
else:
    interface_ip_differences = diff_list2_list1(get_static_interface_ip_list(),get_dynamic_interface_ip_list())
    if interface_ip_differences:
        print(f"CRITICAL: The following interface ip addresses are present in ifconfig")
        print(f"CRITICAL: However are missing in your static config /etc/network/interfaces or /etc/network/interfaces.d/*:")
        print(f"CRITICAL:{interface_ip_differences}")
        print(f"CRITICAL: If you restart the node you will most likely loose these ip addresses")
    else:
        print(f"No interface ip address differences were found between ifconfig and /etc/network/*")
print ("####Checking for static config that is missing in the dynamic interfaces####")
if get_static_interface_ip_list() == None and get_dynamic_interface_ip_list() == None:
        print(f"No static or dynamic network ip addresses were found to diff")
elif get_static_interface_ip_list() == None:
        print(f"No static network configuration ip addresses were found in /etc/networks/*")
        print(f"Your dynamic network interface ip addresses are listed below")
        print(f"Dynamic network IP addresses: {get_dynamic_interface_ip_list()}")
elif get_dynamic_interface_ip_list() == None: 
        print(f"No dynamic network configuration ip addresses were found")
        print(f"Your static network configuration interface names are listed below")
        print(f"Static network IP addresses: {get_static_interface_ip_list()}")
else:
    interface_ip_differences = diff_list1_list2(get_static_interface_ip_list(),get_dynamic_interface_ip_list())
    if interface_ip_differences:
        print(f"CRITICAL: The following interface ip addresses are present in static config /etc/network/interfaces or /etc/network/interfaces.d/*")
        print(f"CRITICAL: However are missing in ifconfig")
        print(f"CRITICAL:{interface_ip_differences}")
        print(f"CRITICAL: If you restart these new static interfaces may appear and cause a problem")
    else:
        print(f"No interface ip address differences were found between /etc/network/* and ifconfig")

print ("========================================================================================================")
print ("Check the number of static routes in static config matches the number of static routes in dynamic config")
print ("========================================================================================================")
static_static_routes=(get_static_static_routes())
number_of_static_static_routes=len(static_static_routes)
dynamic_static_routes=(get_dynamic_static_routes())
number_of_dynamic_static_routes=len(dynamic_static_routes)
#print ("DEBUG: number_of_static_static_routes.count:", number_of_static_static_routes)
#print ("DEBUG: number_of_dynamic_static_routes.count:", number_of_dynamic_static_routes)
if number_of_static_static_routes != number_of_dynamic_static_routes:
    print (f"CRITICAL:The number of static routes in config /etc/networks/* does not match the number of static routes running in the OS 'ip route show'")
    print (f"CRITICAL:On the next restart you may end up loosing or gaining static routes, which will impact service")
    print (f"CRITICAL:Here are the static routes I can find in your network configuration /etc/networks/*")
    print (static_static_routes)
    print (f"CRITICAL:Here are the static routes I can find in the runing kernel 'ip route show'")
    print (dynamic_static_routes)
    print (f"CRITICAL:You need to look into this")
else:
    print (f"The number of static routes in config vs kernal match")
    print (f"The number of Static routes in config={number_of_static_static_routes}")
    print (f"The number of Static routes running in the kernel={number_of_dynamic_static_routes}")
print ("=====================================================================================")
print ("Audit the static network configuration files in /etc/networks/* against best practise")
print ("=====================================================================================")
#check whether routes are being added with up or post up
print("\n###Check whether we are configuring static routes with 'up' which can be problematic on reboot,  or 'post-up'\n")
if check_static_route_post_up():
    print(f"WARNING: #####Best practise: configuring static routes (1)######") 
    print(f"WARNING: I see these static routes in your configuration files") 
    print(check_static_route_post_up()) 
    print(f"WARNING: So your network configuration files in /etc/networks use 'up route' to create static routes") 
    print(f"WARNING: This can result in timing issues and race conditions where the route is not added on boot/powerup") 
    print(f"WARNING: Best practice would be to use 'post-up' in place of 'up'") 
    print(f"WARNING: 'post-up route or post-up ip route' should also be indented under the interface you wish to add the static route to") 
    print(f"WARNING: Not placed at the end of the file with no indent") 
#check whether routes are being added using net-tools 
print("\n###Check whether routes are being added using net-tools, which is quite old and has been replaced with ip tools\n")
if check_static_route_add():
    print(f"WARNING: #####Best practise: configuring static routes (2)######") 
    print(f"WARNING: I see these static routes in your configuration files") 
    print(check_static_route_post_up()) 
    print(f"WARNING: The 'route add' comand comes from the optional package net-tools") 
    print(f"WARNING: net-tools 'route add' was depreciated  back in 2001, replaced by 'ip route add'") 
    print(f"WARNING: You should consider changing your static routes to use 'ip route add'") 
    print(f"WARNING: Remember to test a restart after the change") 
#check whether jumbo frames are being used 
print("\n###Check whether we are using jumbo frames, or are sending all packets (even intra DCU packets) with a small <1500 MTUs\n")
if check_static_mtu() == None:
    print(f"WARNING: #####Best practise: configuring jumbo frames (mtu 9000)######") 
    print(f"WARNING: I am not seeing any mtu's set in your interface configuration") 
    print(f"WARNING: Which means all of your ethernet packets will have an mtu of 1500 or less") 
    print(f"WARNING: Flow typically arrives with an mtu of 1500 or less anyway") 
    print(f"WARNING: But for example, inter DCU traffic will be working very hard, sending 6x as many packets as it needs to") 
    print(f"WARNING: This is especially problematic for VM's or servers with cheap SW focused  NIC's") 
    print(f"WARNING: Most DC's have supported jumbo frames for many years now") 
    print(f"WARNING: We are running jumbo frames in many of our deployments, you might consider migrating to use the same here") 
else:
    print(f"We are setting mtu in the network static config. This is a good way to reduce the network overhead on the CPU, especually in VM's") 

print ("===========================================================================")
print ("==================================All Done=================================")
print ("===========================================================================")

