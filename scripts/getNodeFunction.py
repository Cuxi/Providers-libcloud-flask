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

		networks = node.extra['network_interfaces']

		networkInterfaces = []
		for network in networks:
			pass

			network_interfaces = {'id' : network.id, 'name' : network.name}

			networkInterfaces.append(network_interfaces)

			extra = {'root_device_type' : node.extra['root_device_type'], 'launch_time' : node.extra['launch_time'],
			'ramdisk_id' : node.extra['ramdisk_id'], 'iam_profile' : node.extra['iam_profile'],
			'availability' : node.extra['availability'], 'source_dest_check' : node.extra['source_dest_check'],
			'monitoring' : node.extra['monitoring'], 'subnet_id' : node.extra['subnet_id'],
			'ebs_optimized' : node.extra['ebs_optimized'], 'instance_tenancy' : node.extra['instance_tenancy'],
			'platform' : node.extra['platform'], 'client_token' : node.extra['client_token'],
			'virtualization_type' : node.extra['virtualization_type'], 'root_device_name' : node.extra['virtualization_type'],
			'status' : node.extra['status'], 'block_device_mapping' : node.extra['block_device_mapping'],
			'kernel_id' : node.extra['kernel_id'], 'key_name' : node.extra['key_name'],
			'image_id' : node.extra['image_id'], 'reason' : node.extra['reason'],
			'groups' : node.extra['groups'], 'instance_lifecycle' : node.extra['instance_lifecycle'],
			'tags' : node.extra['tags'], 'dns_name' : node.extra['dns_name'],
			'network_interfaces' : networkInterfaces, 'launch_index' : node.extra['launch_index'], 
			'instance_id' : node.extra['instance_id'], 'instance_type' : node.extra['instance_type'],
			'architecture' : node.extra['architecture'], 'hypervisor' : node.extra['hypervisor'],
			'vpc_id' : node.extra['vpc_id'], 'private_dns' : node.extra['private_dns'],
			'product_codes' : node.extra['product_codes']}

			attr = {'id' : node.id, 'name': node.name, 'state' : node.state, 
			'public_ips' : node.public_ips, 'private_ips' : node.private_ips,
			'provider' : 'Amazon', 'extra' : extra} 

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
				idNod = idNodes
	#			print idNod

				nodesProvider = json.dumps(idNod)



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
