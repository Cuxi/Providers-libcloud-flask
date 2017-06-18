#!/usr/bin/python
import json
import sys
import os
import checkStatus
import elasticIP
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.digitalocean import DigitalOceanNodeDriver
from libcloud.compute.drivers.azure_arm import AzureNodeDriver
from libcloud.compute.drivers.ec2 import BaseEC2NodeDriver
from libcloud.compute.drivers.linode import LinodeNodeDriver

def createNode(provider,driverUno,driverDos,driverTres,driverCuatro,name,size,image,location,ex_network):
	pass
	nodesProvider = ''
	if provider == "Digital Ocean":
		pass
		accessKey = driverUno
		sshKey = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		driver = DigitalOceanNodeDriver(accessKey)
		
		sshKeyID = list()

		ssh = int(sshKey)
		keyPairs = driver.list_key_pairs();
		sizesNode = driver.list_sizes()
		imagesNode = driver.list_images()
		locationsNode = driver.list_locations()

		for keyPair in keyPairs:
			if keyPair.extra['id'] == ssh:
				pass
				sshKeyID.append(keyPair.extra['id'])

		for sizeNode in sizesNode:
			if sizeNode.name == size:
				pass
				sizeName = sizeNode

		for imageNode in imagesNode:
			if imageNode.id == image:	
				pass
				imageId = imageNode

		for locationNode in locationsNode:
			if locationNode.id == location:
				pass
				locationId = locationNode

		idNodes = driver.create_node(name, sizeName, imageId, locationId, None, sshKeyID, None)
		idNodes.extra = json.dumps(idNodes.extra)
		attr = {'id' : idNodes.id, 'name' : idNodes.name, 
		'state' : idNodes.state, 'public_ips' : idNodes.public_ips, 
		'private_ips' : idNodes.private_ips, 'provider' : 'DigitalOcean',
		'extra' : idNodes.extra	}

		nodesProvider = json.dumps(attr)
	if provider == "EC2":
		pass
		accessId = driverUno
		secretKey = driverDos
		region = driverTres
		driverCuatro = driverCuatro
		reg = region[0:len(region)-1]
	#	driver = BaseEC2NodeDriver(accessId,secretKey,'eu-west-1')

		cls = get_driver(Provider.EC2)
		driver = cls(accessId, secretKey, region=reg)

		sizesNode = driver.list_sizes()
		imagesNode = driver.list_images()
		


		sizeName = ''
		imageId = ''

		for sizeNode in sizesNode:
			if sizeNode.id == size:
				pass
				sizeName = sizeNode

		for imageNode in imagesNode:
			if imageNode.name == image:	
				pass
				imageId = imageNode

		nodeCreate = driver.create_node(name = name, image = imageId, size = sizeName)

		types = 'running'

		node = checkStatus.checkStatus(driver, nodeCreate.id, types)

		if node != 0:
			pass
			elastic = elasticIP.setElasticIP(driver,node.id)
			if elastic != 0:
				pass
				v4 = []
				ips = {'ipaddress' : elastic.ip, 'gateway' : 'NULL', 'mask' : 'NULL', 'private_ip' : node.private_ips[0]}

				v4.append(ips)

				network = {'v4' : v4}


				extra = {'launch_time' : node.extra['launch_time'], 'instance_type' : node.extra['instance_type'],
				'network' : network}

				attr = {'id' : node.id, 'region' : reg, 'name': node.name, 'state' : node.state, 
				'public_ip' : elastic.ip, 'provider' : 'Amazon', 'extra' : extra} 

				print json.dumps(attr)
			else:
				v4 = []
				ips = {'ipaddress' : node.public_ips[0], 'gateway' : 'NULL', 'mask' : 'NULL', 'private_ip' : node.private_ips[0]}

				v4.append(ips)

				network = {'v4' : v4}


				extra = {'launch_time' : node.extra['launch_time'], 'instance_type' : node.extra['instance_type'],
				'network' : network}

				attr = {'id' : node.id, 'region' : region, 'name': node.name, 'state' : node.state, 
				'public_ip' : node.public_ips[0], 'provider' : 'Amazon', 'extra' : extra, 'elastic' : '0'}

			nodesProvider = json.dumps(attr)

	if provider == "Azure":
		pass
		tenantId = driverUno
		subscriptionId = driverDos
		applicationId = driverTres
		keyPaswd = driverCuatro
		driver = AzureNodeDriver(tenantId,subscriptionId,applicationId,keyPaswd)

		locations = driver.list_locations()
		networks = driver.ex_list_networks()

		for network in networks:
			pass
			if network.name == ex_network:
				pass
				ex_network = network

		for loc in locations:
			pass
			if loc.id == location:
				pass
				locationID = loc

		sizesNode = driver.list_sizes(location=locationID)
		imagesNode = driver.list_images(location=locationID, ex_publisher=None, ex_offer=None, ex_sku=None, ex_version=None)
		for sizeNode in sizesNode:
			if sizeNode.name == size:
				pass
				sizeName = sizeNode

		for imageNode in imagesNode:
			if imageNode.id == image:	
				pass
				imageId = imageNode

		
		nodeCreate = driver.create_node(name, sizeName, imageId, None, 
			None, None,location = locationID,
			ex_network = ex_network, ex_subnet= None, ex_nic=None)

		types = 'running'

		node = checkStatus.checkStatus(driver, nodeCreate.id, types)

		if node != 0:
			pass
			v4 = []
			ips = {'ipaddress' : node.public_ips, 'gateway' : 'NULL', 'mask' : 'NULL', 'private_ip' : node.private_ips}

			v4.append(ips)

			network = {'v4' : v4}


			extra = {'instance_type' : node.extra['properties']['hardwareProfile']['vmSize'],
			'network' : network}

			attr = {'id' : node.extra['properties']['vmId'], 'region' : node.extra['location'], 'name': node.name, 'state' : node.state, 
			'public_ip' : node.public_ips, 'provider' : 'Azure Virtual machines', 'extra' : extra} 

			nodesProvider = json.dumps(attr)


	if provider == "Linode":
		pass
		apiKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		nodeId = nodeId
		driver = LinodeNodeDriver(apiKey)

		node = driver.create_node(name, image, size, auth, location)
		nodesProvider = json.dumps(node)

		
	return nodesProvider