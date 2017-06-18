#!/usr/bin/python
import json
import sys
import os
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.digitalocean import DigitalOceanNodeDriver
from libcloud.compute.drivers.azure_arm import AzureNodeDriver
from libcloud.compute.drivers.ec2 import BaseEC2NodeDriver
from libcloud.compute.drivers.linode import LinodeNodeDriver

def getAllNodes(provider,driverUno,driverDos,driverTres,driverCuatro):
	pass
	nodesProvider = ''
	node = []
	if provider == "Digital Ocean":
		pass
		accessKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		driver = DigitalOceanNodeDriver(accessKey)
		
		idsNodes = driver.list_nodes()
		
		for idNodes in idsNodes:
			#print idsNodes
			pass
			idNodes.extra = json.dumps(idNodes.extra);
			attr = {'id' : idNodes.id, 'name' : idNodes.name, 
			'state' : idNodes.state, 'public_ips' : idNodes.public_ips, 
			'private_ips' : idNodes.private_ips, 'provider' : 'DigitalOcean',
			'extra' : idNodes.extra	}

			node.append(attr)

		nodesProvider = json.dumps(attr)
	if provider == "EC2":
		pass
		accessId = driverUno
		secretKey = driverDos
		region = driverTres
		driverCuatro = driverCuatro
	#	driver = BaseEC2NodeDriver(accessId,secretKey,'eu-west-1')

		cls = get_driver(Provider.EC2)
		driver = cls(accessId, secretKey, region=region)

		nodes = driver.list_nodes()

		nodeFunction = []
		for node in nodes:
			pass
			if node.state != 'terminated':

				v4 = []
				ips = {'ipaddress' : node.public_ips[0], 'gateway' : 'NULL', 'mask' : 'NULL', 'private_ip' : node.private_ips[0]}

				v4.append(ips)

				network = {'v4' : v4}


				extra = {'launch_time' : node.extra['launch_time'], 'instance_type' : node.extra['instance_type'],
				'network' : network}

				attr = {'id' : node.id, 'region' : region, 'name': node.name, 'state' : node.state, 
				'public_ip' : node.public_ips[0], 'provider' : 'Amazon', 'extra' : extra} 

				nodeFunction.append(json.dumps(attr))
		nodesProvider = nodeFunction

	if provider == "Azure":
		pass
		tenantId = driverUno
		subscriptionId = driverDos
		applicationId = driverTres
		keyPaswd = driverCuatro
		driver = AzureNodeDriver(tenantId,subscriptionId,applicationId,keyPaswd)

		nodes = driver.list_nodes()

		print nodes

	if provider == "Linode":
		pass
		apiKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		driver = LinodeNodeDriver(apiKey)

		nodes = driver.list_nodes()

		nodesProvider = nodes
	return nodesProvider



	