# Providers-libcloud-flask

# Table of contents

1. [Flask microframework Introduction](#flask-microframework-introduction)
2. [How to Work with the Code](#how-to-work-with-the-code)
      * [Installation](#installation)
3. [Scripts](#scripts)
      * [Explaining variables in differents providers](#explaining-variables-in-differents-providers)
            1. [Digital Ocean](#digital-ocean)
            2. [Amazon](#amazon)
            3. [Azure](#azure)

## Flask microframework Introduction

This is a project to use in python with Libcloud's library compute, to create, resize, stop, start, delete and get information of Virtual Machines that we want to have in their cloud compute.  

You can see libcloud's files:

-Azure : [azure_arm](https://github.com/apache/libcloud/blob/trunk/libcloud/compute/drivers/azure_arm.py)

-Amazon : [EC2](https://github.com/apache/libcloud/blob/trunk/libcloud/compute/drivers/ec2.py)

-Digital Ocean : [DO](https://github.com/apache/libcloud/blob/trunk/libcloud/compute/drivers/digitalocean.py)


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

## Scripts

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


### Explaining variables in differents providers

Then, you can see how it works and the differents parts of scripts:

#### Digital Ocean
  
  * Variables for connecting with the provider
  
    driverUno : access Key
  
  * GetNode
    
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/GetNode
    ```
    You need to get your Virtual Machine's information a Node's ID (variable nodeId).
    
  * DeleteNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/DeleteNode
    ```
    You need to delete your Virtual Machine a Node's ID (variable nodeId).
  
  * ShutdownNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/ShutdownNode
    ```
    You need to shutdown your Virtual Machine a Node's ID (variable nodeId).
  
  * StartNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/StartNode
    ```
    You need to start your Virtual Machine a Node's ID (variable nodeId).
  
  * RebootNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/RebootNode
    ```
    You need to reboot your Virtual Machine a Node's ID (variable nodeId).
  
  * ResizeNode
    
    To use this method you need to add the method resize_node from [resize_node.py](https://github.com/Cuxi/Providers-libcloud-flask/blob/master/scripts/resize_node.py) in your local Digital Ocean's driver.
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"n","driverTres":"n","driverCuatro":"n","size":"1gb","nodeId":"52344842"}' http://localhost:5003/RebootNode
    ```
    You need to resize your Virtual Machine:
    
      -A Node's ID (variable nodeId).
      
      -A Size's name (variable size).
  
  * CreateNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key",   "driverDos":"888888","driverTres":"n","driverCuatro":"n","name":"testFlask","size":"512mb","image":"25092162","ex_resource_group":"n","location":"nyc1","ex_network":"n"}' http://localhost:5003/CreateNode
    ```
    You need to create your Virtual Machine (node):
    
      -A ssh key (variable driverDos).
      
      -A name for your node (variable name).
      
      -A Size's name (variable size).
      
      -A image's ID (variable image).
      
      -A location for your node (variable location).  
  
#### Amazon

*Remember that in the case of the Region you must write the id of the datacenter, like us-east-1a*

  * Variables for connecting with the provider
  
    driverUno : Access Key ID
    
    driverDos : Secret Key
    
    driverTres : Region
  
  * GetNode
    
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/GetNode
    ```
    You need to get your Virtual Machine's information a Node's ID (variable nodeId).
    
  * DeleteNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/DeleteNode
    ```
    You need to delete your Virtual Machine a Node's ID (variable nodeId).
  
  * ShutdownNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/ShutdownNode
    ```
    You need to shutdown your Virtual Machine a Node's ID (variable nodeId).
  
  * StartNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/StartNode
    ```
    You need to start your Virtual Machine a Node's ID (variable nodeId).
  
  * RebootNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","nodeId":"52344842"}' http://localhost:5003/RebootNode
    ```
    You need to reboot your Virtual Machine a Node's ID (variable nodeId).
  
  * ResizeNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","size":"1gb","nodeId":"52344842"}' http://localhost:5003/RebootNode
    ```
    You need to resize your Virtual Machine:
    
      -A Node's ID (variable nodeId).
      
      -A Size's name (variable size).
  
  * CreateNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"EC2","driverUno":"your access key ID","driverDos":"your secret key","driverTres":"your region","driverCuatro":"n","name":"testFlask","size":"t2.micro","image":"amzn-ami-hvm-2017.03.0.201","ex_resource_group":"n","location":"n","ex_network":"n"}' http://localhost:5003/CreateNode
    ```
    You need to create your Virtual Machine (node):
      
      -A name for your node (variable name).
      
      -A Size's name (variable size).
      
      -A image's ID (variable image).


#### Azure

  * Variables for connecting with the provider
  
    driverUno : Directory ID (Tenant ID )
    
    driverDos : ID Subscription
    
    driverTres : Application ID
    
    driverCuatro : Key (Password)
  
  * GetNode
    
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/GetNode
    ```
    You need to get your Virtual Machine's information a Node's ID (variable nodeId).
    
  * DeleteNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/DeleteNode
    ```
    You need to delete your Virtual Machine a Node's ID (variable nodeId).
  
  * ShutdownNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/ShutdownNode
    ```
    You need to shutdown your Virtual Machine a Node's ID (variable nodeId).
  
  * StartNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/StartNode
    ```
    You need to start your Virtual Machine a Node's ID (variable nodeId).
  
  * RebootNode
  
    ```
    curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Azure","driverUno":"your tenant ID","driverDos":"your subscription ID","driverTres":"your application ID","driverCuatro":"your password key","nodeId":"52344842"}' http://localhost:5003/RebootNode
    ```
    You need to reboot your Virtual Machine a Node's ID (variable nodeId).
  
  * CreateNode
  
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
      
