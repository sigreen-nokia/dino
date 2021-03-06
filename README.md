 
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
	dino - Deepfield customer engineer trainer
	-------------------------------------------------

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
            14.Exit

	-------------------------------------------------
	Deepfield Cluster Health
	-------------------------------------------------

            1.salt-ping all nodes                          #tests basic connectivity Master to each worker
            2.soup status on all nodes                     #checks the status of the Deepfield processes
            3.check disk space                             #show disk space available per partition for all nodes    
            4.memory hogs                                  #show the top processes consuming memory for all nodes 
            5.cpu hogs                                     #show the top processes consuming cpu for all nodes 
            6.show me the cpu details for each node        #cpu details
            7.show me the cpu model for each node          #cpu model
            8.get the cpu clock speeds for each node       #wondering why one node is busy.. perhaps you have a fan out and the clock was stepped
            9.Return


	-------------------------------------------------
	Deepfield Queries the customer is using most frequently (view optimization)
	-------------------------------------------------

            1.Show the most frequently ran customer queries in contexts traffic,backbone,big_cube 
            2.Show the most frequently ran customer queries in context subscriber
            3.Show the most frequently ran customer queries in context video_stream
            4.Show the most frequently ran customer queries in context flowdump
            5.Cleanup the /tmp/dino-* directories used to store the queries
            6.Return

	-------------------------------------------------
	Deepfield Networking
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
            13.Return

....and can click through the menu's in order to execute tasks

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

## How can I add new steps

* edit the code and commit to master    
* email simon.green and ask if he can add it for you 





