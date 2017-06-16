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

def createNode(provider,driverUno,driverDos,driverTres,driverCuatro,name,size,image,location,ex_storage_account):
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
	#	driver = BaseEC2NodeDriver(accessId,secretKey,'eu-west-1')

		cls = get_driver(Provider.EC2)
		driver = cls(accessId, secretKey, region=region)

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

		node = driver.create_node(name = name, image = imageId, size = sizeName)

		status = checkStatus.checkStatus(driver, node.id)

		if status == 1:
			pass
			print elasticIP.setElasticIP(driver,node.id)

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
		ex_resource_group = location
		driver = AzureNodeDriver(tenantId,subscriptionId,applicationId,keyPaswd)

		sizesNode = driver.list_sizes()
		imagesNode = driver.list_images()

		for sizeNode in sizesNode:
			if sizeNode.name == size:
				pass
				sizeName = sizeNode

		for imageNode in imagesNode:
			if imageNode.id == image:	
				pass
				imageId = imageNode

		
		node = driver.create_node(name, sizeName, imageId, None, ex_resource_group, ex_storage_account)
		nodesProvider = json.dumps(node)



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