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

def getNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId):
	pass
	nodesProvider = ''
	if provider == "Digital Ocean":
		pass
		accessKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		nodeId = nodeId
		driver = DigitalOceanNodeDriver(accessKey)
		
		idsNodes = driver.list_nodes()
		
		for idNodes in idsNodes:
		#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod
				idNod.extra = json.dumps(idNod.extra);
				attr = {'id' : idNod.id, 'name' : idNod.name, 
				'state' : idNod.state, 'public_ips' : idNod.public_ips, 
				'private_ips' : idNod.private_ips, 'provider' : 'DigitalOcean',
				'extra' : idNod.extra}

				nodesProvider = json.dumps(attr)
	if provider == "EC2":
		pass
		accessId = driverUno
		secretKey = driverDos
		region = driverTres
		driverCuatro = driverCuatro
		nodeId = nodeId
	#	driver = BaseEC2NodeDriver(accessId,secretKey,'eu-west-1')

		cls = get_driver(Provider.EC2)
		driver = cls(accessId, secretKey, region=region)

		idsNodes = driver.list_nodes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				node = idNodes

				if node.state == 'terminated':
					v4 = []
					ips = {'ipaddress' : node.public_ips, 'gateway' : 'NULL', 'mask' : 'NULL', 'private_ip' : node.private_ips}

					v4.append(ips)

					network = {'v4' : v4}


					extra = {'launch_time' : node.extra['launch_time'], 'instance_type' : node.extra['instance_type'],
					'network' : network}

					attr = {'id' : node.id, 'region' : region, 'name': node.name, 'state' : node.state, 
					'public_ip' : node.public_ips, 'provider' : 'Amazon', 'extra' : extra}
				if node.state != 'terminated':
					v4 = []
					ips = {'ipaddress' : node.public_ips[0], 'gateway' : 'NULL', 'mask' : 'NULL', 'private_ip' : node.private_ips[0]}

					v4.append(ips)

					network = {'v4' : v4}


					extra = {'launch_time' : node.extra['launch_time'], 'instance_type' : node.extra['instance_type'],
					'network' : network}

					attr = {'id' : node.id, 'region' : region, 'name': node.name, 'state' : node.state, 
					'public_ip' : node.public_ips[0], 'provider' : 'Amazon', 'extra' : extra} 

			nodesProvider = json.dumps(attr)
	if provider == "Azure":
		pass
		tenantId = driverUno
		subscriptionId = driverDos
		applicationId = driverTres
		keyPaswd = driverCuatro
		nodeId = nodeId
		driver = AzureNodeDriver(tenantId,subscriptionId,applicationId,keyPaswd)

		idsNodes = driver.list_nodes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				node = idNodes
	#			print idNod
				v4 = []
				ips = {'ipaddress' : node.public_ips, 'gateway' : 'NULL', 'mask' : 'NULL', 'private_ip' : node.private_ips}

				v4.append(ips)

				network = {'v4' : v4}


				extra = {'instance_type' : node.extra['properties']['hardwareProfile']['vmSize'],
				'network' : network}

				attr = {'id' : node.extra['properties']['vmId'], 'region' : node.extra['location'], 'name': node.name, 'state' : node.state, 
				'public_ip' : node.public_ips, 'provider' : 'Azure Virtual machines', 'extra' : extra} 

				nodesProvider = json.dumps(node)

	if provider == "Linode":
		pass
		apiKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		nodeId = nodeId
		driver = LinodeNodeDriver(apiKey)

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod

				nodesProvider = json.dumps(idNod)

	return nodesProvider

