# Providers-libcloud-flask

# Table of contents

1. [Flask microframework Introduction](#flask-microframework-introduction)
2. [How to Work with the Code](#how-to-work-with-the-code)
      * [Installation](#installation)
3. [Methods](#methods)
     * [Curl request](#curl-request)
      1. [Digital Ocean](#digital-ocean)
      2. [Amazon](#amazon)
      3. [Azure](#azure)
     * [Response](#response)

## Flask microframework Introduction

This is a project to use in python with Libcloud's library compute, to create, resize, stop, start, delete and get information of Virtual Machines that we want to have in their cloud compute.  

You can see libcloud's files:

-[Azure](https://github.com/apache/libcloud/blob/trunk/libcloud/compute/drivers/azure_arm.py)

-[Amazon](https://github.com/apache/libcloud/blob/trunk/libcloud/compute/drivers/ec2.py)

-[Digital Ocean](https://github.com/apache/libcloud/blob/trunk/libcloud/compute/drivers/digitalocean.py)


## How to Work with the Code

Clone this repository:

```
git clone https://github.com/Cuxi/Providers-libcloud-flask.git
```

Clone Libcloud's repository, or install in your pc:

Visit [Libcloud Page](http://libcloud.readthedocs.io/en/latest/getting_started.html).

If you want to use Digital Ocean's resize, it's better if you install Libcloud (Libcloud has no method to resize already).

### Installation

The first of all you need to install [python](https://gist.github.com/nikcub/49885e62cf8b0bff8cf9780aeb2bf7e3).


Continue installing extensions:

```
$ pip install <name_ext>
```

* flask
* flask-restful

## Methods

First, you must do is run our flask script functions.py in your localhost with this command:
```
python functions.py
```

To execute the scripts you need to execute a command curl, for example:

```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"name of the provider","driverUno":$driverUno, "driverDos":$driverDos,"driverTres":$driverTres,"driverCuatro":$driverCuatro}' http://localhost:5003/GetLocations
```

There are scripts, where some provider don't need all the variables, so in that case put a letter as the variable. For example:

```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key", "driverDos":"n","driverTres":"n","driverCuatro":"n"}' http://localhost:5003/GetLocations
```


### Curl request

Then, you can see how it works and the differents parts of scripts:

#### Digital Ocean

1. [Variables for connecting with the provider](#variables-for-connecting-with-the-provider)
2. [GetNode](#getnode)
3. [DeleteNode](#deletenode)
4. [ShutdownNode](#shutdownnode)
5. [StartNode](#startnode)
6. [RebootNode](#rebootnode)
7. [ResizeNode](#resizenode)
8. [CreateNode](#createnode)
9. [GetAllNodes](#getAllnodes)
10. [GetLocations](#getlocations)
  
  ##### Variables for connecting with the provider
  
    driverUno : access Key
  
  ##### GetNode
    
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/GetNode
```
You need to get your Virtual Machine's information a Node's ID (variable nodeId).
    
  ##### DeleteNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/DeleteNode
```
You need to delete your Virtual Machine a Node's ID (variable nodeId).
  
  ##### ShutdownNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/ShutdownNode
```
You need to shutdown your Virtual Machine a Node's ID (variable nodeId).
  
  ##### StartNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/StartNode
```
You need to start your Virtual Machine a Node's ID (variable nodeId).
  
  ##### RebootNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/RebootNode
```
You need to reboot your Virtual Machine a Node's ID (variable nodeId).
  
  ##### ResizeNode
    
To use this method you need to add the method resize_node from [resize_node.py](https://github.com/Cuxi/Providers-libcloud-flask/blob/master/scripts/resize_node.py) in your local Digital Ocean's driver.

```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","size":"1gb","nodeId":"52344842"}' http://localhost:5003/RebootNode
```
You need to resize your Virtual Machine:

 -A Node's ID (variable nodeId).

 -A Size's name (variable size).
  
  ##### CreateNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"888888","driverTres":"n","driverCuatro":"n","name":"testFlask","size":"512mb","image":"25092162","ex_resource_group":"n","location":"nyc1","ex_network":"n"}' http://localhost:5003/CreateNode
```
You need to create your Virtual Machine (node):

 -A ssh key (variable driverDos).

 -A name for your node (variable name).

 -A Size's name (variable size).

 -A image's ID (variable image).

 -A location for your node (variable location).  
   
  ##### GetAllNodes
 
 ```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n"}' http://localhost:5003/GetAllNodes
```
As you can see, you just need to pass access parameters.

  ##### GetLocations
 
 ```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n"}' http://localhost:5003/GetLocations
```
As you can see, you just need to pass access parameters.
  
#### Amazon

*Remember that in the case of the Region you must write the id of the datacenter, like us-east-1a*

1. [Variables for connecting with the provider](#variables-for-connecting-with-the-provider-1)
2. [GetNode](#getnode-1)
3. [DeleteNode](#deletenode-1)
4. [ShutdownNode](#shutdownnode-1)
5. [StartNode](#startnode-1)
6. [RebootNode](#rebootnode-1)
7. [ResizeNode](#resizenode-1)
8. [CreateNode](#createnode-1)
9. [GetAllNodes](#getAllnodes-1)
10. [GetLocations](#getlocations-1)

  ##### Variables for connecting with the provider
  
driverUno : Access Key ID

driverDos : Secret Key

driverTres : Region
  
  ##### GetNode
    
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"i-0b8a2c5eb0314840d"}' http://localhost:5003/GetNode
```
You need to get your Virtual Machine's information a Node's ID (variable nodeId).
    
  ##### DeleteNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"i-0b8a2c5eb0314840d"}' http://localhost:5003/DeleteNode
```
You need to delete your Virtual Machine a Node's ID (variable nodeId).
  
  ##### ShutdownNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"i-0b8a2c5eb0314840d"}' http://localhost:5003/ShutdownNode
```
You need to shutdown your Virtual Machine a Node's ID (variable nodeId).
  
  ##### StartNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"i-0b8a2c5eb0314840d"}' http://localhost:5003/StartNode
```
You need to start your Virtual Machine a Node's ID (variable nodeId).
  
  ##### RebootNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"i-0b8a2c5eb0314840d"}' http://localhost:5003/RebootNode
```
You need to reboot your Virtual Machine a Node's ID (variable nodeId).
  
  ##### ResizeNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","size":"t2.small","nodeId":"i-0b8a2c5eb0314840d"}' http://localhost:5003/RebootNode
```
You need to resize your Virtual Machine:

 -A Node's ID (variable nodeId).

 -A Size's name (variable size).
  
  ##### CreateNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","name":"testFlask","size":"t2.micro","image":"amzn-ami-hvm-2017.03.0.201","ex_resource_group":"n","location":"n","ex_network":"n"}' http://localhost:5003/CreateNode
```
You need to create your Virtual Machine (node):

 -A name for your node (variable name).

 -A Size's name (variable size).

 -A image's ID (variable image).
 
  ##### GetAllNodes
 
 ```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n"}' http://localhost:5003/GetAllNodes
```
As you can see, you just need to pass access parameters.

  ##### GetLocations
 
 ```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"n","driverCuatro":"n"}' http://localhost:5003/GetLocations
```
As you can see, you just need to pass access parameters. But not passing the region in driverTres.


#### Azure

1. [Variables for connecting with the provider](#variables-for-connecting-with-the-provider-2)
2. [GetNode](#getnode-2)
3. [DeleteNode](#deletenode-2)
4. [ShutdownNode](#shutdownnode-2)
5. [StartNode](#startnode-2)
6. [RebootNode](#rebootnode-2)
7. [ResizeNode](#resizenode-2)
8. [CreateNode](#createnode-2)
9. [GetAllNodes](#getAllnodes-2)
10. [GetLocations](#getlocations-2)

  ##### Variables for connecting with the provider
  
driverUno : Directory ID (Tenant ID )

driverDos : ID Subscription

driverTres : Application ID

driverCuatro : Key (Password)
  
  ##### GetNode
    
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/GetNode
```
You need to get your Virtual Machine's information a Node's ID (variable nodeId).
    
  ##### DeleteNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/DeleteNode
```
You need to delete your Virtual Machine a Node's ID (variable nodeId).
  
  ##### ShutdownNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/ShutdownNode
```
You need to shutdown your Virtual Machine a Node's ID (variable nodeId).
  
  ##### StartNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/StartNode
```
You need to start your Virtual Machine a Node's ID (variable nodeId).
  
  ##### RebootNode
  
```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/RebootNode
```
You need to reboot your Virtual Machine a Node's ID (variable nodeId).
  
  ##### CreateNode
  
At moment this method is not working, there is a problem in library.

```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","name":"testFlask","size":"Basic_A0","image":"RightScaleLinex:RightImage-Ubuntu:14.04:14.2.1","ex_resource_group":"exampleName","location":"westeurope","ex_network":"exampleName"}' http://localhost:5003/CreateNode
```
You need to create your Virtual Machine (node):

 -A name for your node (variable name).

 -A Size's name (variable size).

 -A image's ID (variable image).

 -A Resource Group's name (variable ex_resource_group).

 -A location for your node (variable location).

 -A Network's name for your node (variable ex_network)

  ##### GetAllNodes
 
 ```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key"}' http://localhost:5003/GetAllNodes
```
As you can see, you just need to pass access parameters.

  ##### GetLocations
 
 ```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key"}' http://localhost:5003/GetLocations
```
As you can see, you just need to pass access parameters.
      
### Response

1. [Boolean](#boolean)
2. [Node's information](#nodeslocation)
3. [Locations' information](#locationsinformation)

At last but not least, the responses. As you can see if you have made come curl to this api, there are four types of response.

We can make three types of groups depends of response:

#### Boolean

The motehods that return a boolean are: [DeleteNode](#deletenode), [ShutdownNode](#shutdownnode), [StartNode](#startnode), [RebootNode](#rebootnode) and [ResizeNode](#resizenode).

```
* Hostname was NOT found in DNS cache
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 5003 (#0)
> POST /ShutdownNode HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:5003
> Accept: */*
> Content-Type: application/json
> Content-Length: 184
> 
* upload completely sent off: 184 out of 184 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 13
< Server: Werkzeug/0.12.2 Python/2.7.6
< Date: Sun, 18 Jun 2017 17:21:08 GMT
< 
[
    true
]
* Closing connection 0
```

#### Node's information

The motehods that return a object/s of node/s are: [GetNode](#getnode), [CreateNode](#createnode) and [GetAllNodes](#getallnodes).

```
* Hostname was NOT found in DNS cache
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 5003 (#0)
> POST /GetAllNodes HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:5003
> Accept: */*
> Content-Type: application/json
> Content-Length: 153
> 
* upload completely sent off: 153 out of 153 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 410
< Server: Werkzeug/0.12.2 Python/2.7.6
< Date: Sun, 18 Jun 2017 17:17:00 GMT
< 
[
    "{\"name\": \"testFlask\", \"extra\": {\"instance_type\": \"t2.micro\", \"launch_time\": \"2017-06-18T17:07:55.000Z\", \"network\": {\"v4\": [{\"mask\": \"NULL\", \"ipaddress\": \"34.202.163.22\", \"gateway\": \"NULL\", \"private_ip\": \"172.31.7.60\"}]}}, \"region\": \"us-east-1\", \"public_ip\": \"34.202.163.22\", \"state\": \"running\", \"provider\": \"Amazon\", \"id\": \"i-0b8a2c5eb0314840d\"}"
]
* Closing connection 0
```

#### Locations' information

The motehod that return an object of locations is: [GetLocations](#getlocations).

```
* Hostname was NOT found in DNS cache
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 5003 (#0)
> POST /GetLocations HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:5003
> Accept: */*
> Content-Type: application/json
> Content-Length: 165
> 
* upload completely sent off: 165 out of 165 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 1123
< Server: Werkzeug/0.12.2 Python/2.7.6
< Date: Sun, 18 Jun 2017 16:57:24 GMT
< 
[
    "[{\"country\": \"null\", \"datacenter\": [{\"id\": \"nyc1\", \"name\": \"New York 1\"}, {\"id\": \"nyc2\", \"name\": \"New York 2\"}, {\"id\": \"nyc3\", \"name\": \"New York 3\"}], \"city\": \"New York\"}, {\"country\": \"null\", \"datacenter\": [{\"id\": \"sfo1\", \"name\": \"San Francisco 1\"}, {\"id\": \"sfo2\", \"name\": \"San Francisco 2\"}], \"city\": \"San Francisco\"}, {\"country\": \"null\", \"datacenter\": [{\"id\": \"ams2\", \"name\": \"Amsterdam 2\"}, {\"id\": \"ams3\", \"name\": \"Amsterdam 3\"}], \"city\": \"Amsterdam \"}, {\"country\": \"null\", \"datacenter\": [{\"id\": \"sgp1\", \"name\": \"Singapore 1\"}], \"city\": \"Singapore \"}, {\"country\": \"null\", \"datacenter\": [{\"id\": \"lon1\", \"name\": \"London 1\"}], \"city\": \"London \"}, {\"country\": \"null\", \"datacenter\": [{\"id\": \"fra1\", \"name\": \"Frankfurt 1\"}], \"city\": \"Frankfurt \"}, {\"country\": \"null\", \"datacenter\": [{\"id\": \"tor1\", \"name\": \"Toronto 1\"}], \"city\": \"Toronto \"}, {\"country\": \"null\", \"datacenter\": [{\"id\": \"blr1\", \"name\": \"Bangalore 1\"}], \"city\": \"Bangalore \"}]"
]
* Closing connection 0
```
