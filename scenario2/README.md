# Second scenario

In fact this instance is a loadbalancer with SSL termination on it.
When monitor load balancer next metrics are important:

* Latency - represents how long it takes for your service to process a request. 
  Specifically, it’s the time from when a request leaves the load balancer until it returns.
  There is no "correct" value for latency. It’s a reflection of your service and the problem your service addresses. 
  In general, latency should be as close to zero as possible...but it is ideally.
* Rejected Connections - represents how many client connections were rejected by the load balancer.
  This metric counts the number of requests the load balancer had to reject (or hold and send later) because your target 
  application could no longer service incoming requests.
* 5xx Status Codes - this metric tells us if our service or if the load balancer is failing to process client requests.
  So there are two same metrics - 5xx Status Codes from load balancer itself and from applications as well.
* Target Host Health - metric shows us count of UnHealthy applications.
* Connection Count - Connection count refers to the number of clients connected to our load balancer. 
* Bytes - metric shows us bytes count sent and received from and to load balancer.


We need take into consideration that fact that our load balancer installed on managed instance (which we need maintain).  
It means that we also need to monitor system resources as well. SSL termination is a CPU intensive task and we need 
monitor at least:

* CPU utilization
* Load Average

Payload which will be sent via load balancer involves RAM into workflow and we need provide RAM monitoring as well.

Load average can be improved by monitoring IO because of it could be a reason of processes stucked in queue to CPU.

So, system metrics from instance which we need to monitor:

* CPU utilization
* Load Average
* RAM (Physical, Virt, Cache, Buffer)
* IO (writes/reads)
* disks size

Most of software load balancers provides endpoint with load balancer's related metrics. So we need simply scrape this 
endpoint and manage these metrics (collect them if needed/fire alerts on threshold).

For system metrics we could use any monitoring agents (prometheus exporter, datadog agent, zabbix agent etc...)  
As for challenges:

* One instance could be not enough for our needs and we need to think about scaling based on above metrics.
* Design of monitoring will depends on how we will use our 2 NICs.
* Ideally to implement one monitoring solution for both system's and load balancer's metrics.


Not sure how deep I need to dive into this scenario. Will stop on this stage of diving.