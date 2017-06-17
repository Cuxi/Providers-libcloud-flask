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

def resizeNode(provider,driverUno,driverDos,driverTres,driverCuatro,size,nodeId):
	pass
	nodesProvider = ''
	if provider == "Digital Ocean":
		pass
		accessKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		size = size
		nodeId = nodeId
		driver = DigitalOceanNodeDriver(accessKey)
		
		idsNodes = driver.list_nodes()
		sizesNode = driver.list_sizes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod

		for sizeNode in sizesNode:
			if sizeNode.name == size:
				pass
				sizeName = sizeNode

				nodesProvider = driver.resize_node(sizeName, idNod)

	if provider == "EC2":
		pass
		accessId = driverUno
		secretKey = driverDos
		region = driverTres
		driverCuatro = driverCuatro
		size = size
		nodeId = nodeId
	#	driver = BaseEC2NodeDriver(accessId,secretKey,'eu-west-1')

		cls = get_driver(Provider.EC2)
		driver = cls(accessId, secretKey, region=region)

		idsNodes = driver.list_nodes()
		sizesNode = driver.list_sizes()

		idNod = ''
		sizeName = ''

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod

		for sizeNode in sizesNode:
			if sizeNode.id == size:
				pass
				sizeName = sizeNode

		nodesProvider = driver.ex_change_node_size(idNod, sizeName)
	if provider == "Azure":
		pass
		tenantId = driverUno
		subscriptionId = driverDos
		applicationId = driverTres
		keyPaswd = driverCuatro
		size = size
		nodeId = nodeId
		driver = AzureNodeDriver(tenantId,subscriptionId,applicationId,keyPaswd)

		idsNodes = driver.list_nodes()
		sizesNode = driver.list_sizes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod

		for sizeNode in sizesNode:
			if sizeNode.name == size:
				pass
				sizeName = sizeNode

				nodesProvider = driver.resize_node(sizeName, idNod)



	if provider == "Linode":
		pass
		apiKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		size = size
		nodeId = nodeId
		driver = LinodeNodeDriver(apiKey)

		idsNodes = driver.list_nodes()
		sizesNode = driver.list_sizes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod

		for sizeNode in sizesNode:
			if sizeNode.name == size:
				pass
				sizeName = sizeNode

				nodesProvider = driver.ex_resize_node(sizeName, idNod)

	return nodesProvider