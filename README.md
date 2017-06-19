# Providers-libcloud-flask

## Flask microframework Introduction

### How to Work with the Code

Clone this repository:

```
git clone https://github.com/Cuxi/Providers-libcloud-flask.git
```

Clone Libcloud's repository, or install in your pc:

Visit [Libcloud Page](http://libcloud.readthedocs.io/en/latest/getting_started.html).

If you want to use Digital Ocean's resize, it's better if you install Libcloud (Libcloud has no method to resize already).

**Flask extensions or python packages that you should install**

To install extensions:

```
$ pip install <name_ext>
```

* flask
* flask-restful

## Scripts

To execute the scripts you need to execute a command curl, for example:

```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"name of the provider","driverUno":$driverUno, "driverDos":$driverDos,"driverTres":$driverTres,"driverCuatro":$driverCuatro}' http://localhost:5003/GetLocations
```

There are scripts, where some provider don't need all the variables, so in that case put a letter as the variable. For example:

```
curl -v -X POST  -H 'Content-Type: application/json' -d '{"provider":"Digital Ocean","driverUno":"your access key", "driverDos":"n","driverTres":"n","driverCuatro":"n"}' http://localhost:5003/GetLocations
```


### Explaining variables in differents providers

Then we're showing you the needed variables in scripts.

**Digital Ocean**
  
  * In common 
  
  DriverUno : access Key
  
  * GetNode, DeleteNode, ShutdownNode, StartNode and RebootNode
  
  NodeId : Virtual Machine's ID
  
  * ResizeNode
  
  NodeId : Virtual Machine's ID
  
  Size : Virtual Machine's size ID
  
  * CreateNode
  
  DriverDos : SSH Key 
  
  Size : Virtual Machine's size ID
  
  Image : Image's ID 
  
  Location : Location's ID
  
  
**Amazon**

*Remember that in the case of the Region you must write the id of the datacenter, like us-east-1a*

  * In common 
  
    DriverUno : Access Key ID
    
    DriverDos : Secret Key
    
    DriverTres : Region
  
  * GetNode, DeleteNode, ShutdownNode, StartNode and RebootNode
  
    NodeId : Virtual Machine's ID
  
  * ResizeNode
  
    NodeId : Virtual Machine's ID
    
    Size : Virtual Machine's size ID
  
  * CreateNode
  
    Size : Virtual Machine's size ID
    
    Image : Image's ID 


**Azure**

  * In common
  
    DriverUno : Directory ID (Tenant ID )
    
    DriverDos : ID Subscription
    
    DriverTres : Application ID
    
    DriverCuatro : Key (Password)
  
  * GetNode, DeleteNode, ShutdownNode, StartNode and RebootNode
  
    NodeId : Virtual Machine's ID
  
  * ResizeNode (Int this moments is not aviable this method in Libcloud)
  
    NodeId : Virtual Machine's ID
    
    Size : Virtual Machine's size ID
  
  * CreateNode
  
    Size : Virtual Machine's size ID
    
    Image : Image's ID 
    
    Ex_resource_group : Resource Group's name
    
    Location : Location's ID
    
    Ex_network : Network's name
  
