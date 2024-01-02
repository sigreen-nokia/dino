 
     /@\            \|/   
    `-\ \  ______  - 0 -   
       \ \/ ` /  \  /|\ _   
        \_i / \  |\____//   
          | |==| |=----/   
    ----------------------   

## Whats dino.py:


* dino.py is a trainer intended to teach customer engineers how to write and execute day to day tasks and automations
* A trainers code is not fancy, as its intended to be readable.
* It tells the user how it did the task, so they can do it themselfes
* The code is intended to be shared, improved and reused.
* Its written on top of other peoples code and hints, thanks Ato, thanks Chris thanks everyone
* Its a quick way for Deepfield Customer Engineers to get started with day to day tasks 

## How do I use it 

* drop it onto a Deepfield DCU and run 
* python dino.py 

You will see a menu like this one..   

    	-------------------------------------------------
    	Dino - Deepfield customer engineer trainer
    	-------------------------------------------------
    
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
                21.Exit
    
    
    Enter your choice: 
    
    
    	-------------------------------------------------
    	Deepfield Cluster Health (must be ran on the master)
    	-------------------------------------------------
    
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
                16.Return
    
    
    	-------------------------------------------------
    	Deepfield Cluster Configuration (must be ran on the master)
    	-------------------------------------------------
    
                1.salt roles configured on each node 			#shows the configured services on each node 
                2.who has the dnsflow salt role     			#which dcu's
                3.who has the collector salt role     			#which dcu's
                4.List all configured routers
                5.Return
    
    
    	-------------------------------------------------
    	Deepfield Queries the customer is using most frequently (view optimization, must be ran on the master)
    	-------------------------------------------------
    
                1.Show the most frequently ran customer queries in context traffic 
                2.Show the most frequently ran customer queries in contexts backbone
                3.Show the most frequently ran customer queries in contexts big_cube 
                4.Show the most frequently ran customer queries in context subscriber
                5.Show the most frequently ran customer queries in context video_stream
                6.Show the most frequently ran customer queries in context flowdump
                7.Cleanup the dino-* directories used to store the queries
                8.Return
    
    	-------------------------------------------------
    	postgres (must be ran on the master)
    	-------------------------------------------------
    
                1.List the databases in postgres using psql
                2.List the relations in a selected database (pending)
                3.Count the entries in a selected database for a selected relation (pending)
                4.Dump the entries in a selected database for a selected relation (pending)
                5.postgres database hints 
                6.Return
    
    	-------------------------------------------------
    	Deepfield Kafka (must be ran on the master)
    	-------------------------------------------------
    
                1.list the available kafka consumer groups
                2.show the kafka df-dnsflowd consumer groups
                3.show the kafka df-dnsflow-raw topic and partitions 
                4.show the kafka df-classifyd consumer groups 
                5.show the kafka df-flow topic and partitions 
                6.Return
    
    	-------------------------------------------------
    	Deepfield Networking (must be ran on the master)
    	-------------------------------------------------
    
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
                14.Return
    
    	-------------------------------------------------
    	Deepfield MOPS and Backups (must be ran on the master)
    	-------------------------------------------------
    
                1.create a MOP directory on all DCUs based on todays date
                2.backup the network configuration static and dynamic into the MOP directory, on all DCUs
                3.backup the slice.json into the MOP directory, on all DCUs
                4.backup the soup status into the MOP directory, on Master for all DCUs
                5.delete todays mop directory, on all DCUs
                6.Return
    
    
    	-------------------------------------------------
    	HDFS (must be ran on the master)
    	-------------------------------------------------
    
                1.HDFS Status Report
                2.List all HDFS Dimensions, sorted by size
                3.Return
    
    
    	-------------------------------------------------
    	Devices API
    	-------------------------------------------------
    
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
                15.Return
    
    
    	-------------------------------------------------
    	Data Views
    	-------------------------------------------------
    
                1.Get the data view API Topology Schema
                2.For an example traffic query, show me how to find the data view that was used
                3.Get a list of all data views via the API, write to a file (this is a big list, perhaps the next one is better)
                4.Dump a specific data view, selected from a menu of all configured data views 
                5.Starhub Example Case:Create a new custom ddos data view for regs (high retention) - A step by step using an example
                6.LGU+ Example Case: Create a new custom ddos data view sliced on a custom protection group - A step by step using an example
                7.Create a new data view from a json file - A step by step
                8.Patch an existing data view retention - A step by step
                9.Delete an existing data view
                10.Return
    
    
    	-------------------------------------------------
    	Collecting logs and config files (must be ran on the master)
    	-------------------------------------------------
    
                1.Collect log files and slice.json from all DCUs, make one large tar file on master
                2.Clean up old tar files
                3.Return
    
    
    	-------------------------------------------------
    	Defender (DDoS, def.py must be ran on the master. The api's will work locally or remotely)
    	-------------------------------------------------
    
                1.Build up a def.py report, to gather up the defender configuration and running details
                2.Whats my current running Defender Secure Genome branch version
                3.Get a list of all available Defender Secure Genome versions
                4.Show the Defender Secure Genome version history 
                5.Lookup an ipv4 or ipv6 address in Secure Genome
                6.Read a list of ipv4 or ipv6 addresses and look up each in Secure Genome, output to a file 
                7.Create a custom protection group with ipv4 subnets covering the internet.
                8.Return
    
    
    	-------------------------------------------------
    	Dimensions
    	-------------------------------------------------
    
                1.Dump the json for a dimension, selected from a list of all Dimensions
                2.Add a Dimension from a json file
                3.Create a protected object (custom data view) with subnets covering the internet. Step by step example
                4.Delete a dimension, selected from a list of all provisioned dimensions
                5.Dump the csv for all possitions in a dimension, the dimension is selected from a list of all Dimensions
                6.Return


....and can click through the menu's in order to execute tasks, and see how to do it yourself

    Enter your choice: 9
    Command is:sudo salt \* cmd.run "ntpq -p"
    worker01:
             remote           refid      st t when poll reach   delay   offset  jitter
        ==============================================================================
        *10.22.192.240   10.22.8.132      3 u  273 1024  377    0.819    0.019   2.226
        +10.22.192.241   10.22.8.132      3 u  123 1024  377    0.628    0.088   2.042
         LOCAL(0)        .LOCL.          14 l  36d   64    0    0.000    0.000   0.000
        +master.site. 12.34.567.241    4 u  353 1024  377    0.080   -3.167   8.322
    master:
             remote           refid      st t when poll reach   delay   offset  jitter
        ==============================================================================
        *10.22.192.240   10.22.8.132      3 u    -   64  377    0.464    4.742   1.452
        +10.22.192.241   10.22.8.132      3 u    1   64  377    0.567    3.045   1.431
         LOCAL(0)        .LOCL.          10 l  36d   64    0    0.000    0.000   0.000
    worker02:
             remote           refid      st t when poll reach   delay   offset  jitter
        ==============================================================================
        *10.22.192.240   10.22.8.132      3 u  569 1024  377    1.083  -11.344  15.715
        +10.22.192.241   10.22.8.132      3 u  110 1024  377    1.126   -6.815  12.341
         LOCAL(0)        .LOCL.          14 l  36d   64    0    0.000    0.000   0.000
        +master.ite. 12.34.567.241    4 u  589 1024  377    0.586  -20.116  14.507

 
## Can I install it permanently 

* it may already be installed.. 
* optionaly on the Master run these commands
* cp dino.py /usr/local/sbin/ 
* cp get_context.py /usr/local/sbin/ 
* chmod a+x /usr/local/sbin/dino.py 
* chmod a+x /usr/local/sbin/get_context.py 

## Can I run it locally on my laptop

* Yes you run it elsewhere 
* If for example you run it on your laptop, it will prompt you for the api key and cluster fqdn as it can't derive them
* Menu options using Deepfield API's will still work fine
* Menu options using local tools, salt for example, will just fail with command not found, as they need the master node
* This can be helpfull for customer without master node access, to learn how to use our API's

## How can I add new steps

* edit the code yourself and commit to master    
* or 
* email simon.green and ask if he can add it for you 



