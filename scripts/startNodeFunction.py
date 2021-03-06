#!/usr/bin/python
import json
import sys
import os
import checkStatus
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.digitalocean import DigitalOceanNodeDriver
from libcloud.compute.drivers.azure_arm import AzureNodeDriver
from libcloud.compute.drivers.ec2 import BaseEC2NodeDriver
from libcloud.compute.drivers.linode import LinodeNodeDriver

def startNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId):
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
				nodeStarted = driver.ex_power_on_node(idNod)

				types = 'running'

				node = checkStatus.checkStatus(driver, idNod.id, types)

				if node != 0:
					nodesProvider = nodeStarted

	if provider == "EC2":
		pass
		accessId = driverUno
		secretKey = driverDos
		region = driverTres
		driverCuatro = driverCuatro
		nodeId = nodeId
		reg = region[0:len(region)-1]
	#	driver = BaseEC2NodeDriver(accessId,secretKey,'eu-west-1')

		cls = get_driver(Provider.EC2)
		driver = cls(accessId, secretKey, region=reg)

		idsNodes = driver.list_nodes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				print 'entra'
				idNod = idNodes
	#			print idNod
				nodeStarted = driver.ex_start_node(idNod)

				types = 'running'

				node = checkStatus.checkStatus(driver, idNod.id, types)

				if node != 0:
					nodesProvider = nodeStarted

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
				idNod = idNodes
	#			print idNod
				nodeStarted = driver.ex_start_node(idNod)

				types = 'running'

				node = checkStatus.checkStatusAzure(driver, idNod.id, types)

				if node != 0:
					nodesProvider = nodeStarted


	return nodesProvider
