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

def shutdownNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId):
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
				nodeStopped = driver.ex_shutdown_node(idNod)

				types = 'stopped'

				node = checkStatus.checkStatus(driver, idNod.id, types)

				if node != 0:
					nodesProvider = nodeStopped

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
				idNod = idNodes
	#			print idNod
				nodeStopped = driver.ex_stop_node(idNod)

				types = 'stopped'

				node = checkStatus.checkStatus(driver, idNod.id, types)

				if node != 0:
					nodesProvider = nodeStopped

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
				nodeStopped = driver.ex_stop_node(idNod)

				types = 'stopped'

				node = checkStatus.checkStatus(driver, idNod.id, types)

				if node != 0:
					nodesProvider = nodeStopped



	if provider == "Linode":
		pass
		apiKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		nodeId = nodeId
		driver = LinodeNodeDriver(apiKey)

		idsNodes = driver.list_nodes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod
				nodeStopped = driver.ex_stop_node(idNod)

				types = 'stopped'

				node = checkStatus.checkStatus(driver, idNod.id, types)

				if node != 0:
					nodesProvider = nodeStopped

	return nodesProvider