#!/usr/bin/python
import json
import sys
import os
import re
import getRegionName	
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.digitalocean import DigitalOceanNodeDriver
from libcloud.compute.drivers.azure_arm import AzureNodeDriver
from libcloud.compute.drivers.ec2 import BaseEC2NodeDriver, EC2NodeDriver
from libcloud.compute.drivers.linode import LinodeNodeDriver

def getLocations(provider,driverUno,driverDos,driverTres,driverCuatro):
	pass
	nodesProvider = ''
	if provider == "Digital Ocean":
		pass
		accessKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		driver = DigitalOceanNodeDriver(accessKey)

		listLocations = driver.list_locations()

		nodelocations = []
		for listLocation in listLocations:
			data = []
			flag = False
			matches = re.search(r'[a-zA-Z]{0,}', listLocation.name)

			match = re.search(r'[a-zA-Z]{0,}[ ][a-zA-Z]{0,}', listLocation.name)

			if match:
				region = match.group()
			else:
				region = matches.group()

			for nodelocation in nodelocations:
				if nodelocation['city'] == region:
					datacenter = {'id' : listLocation.id, 'name' : listLocation.name}
					nodelocation['datacenter'].append(datacenter)
					flag = True
			if flag != True:			
				datacenter = {'id' : listLocation.id, 'name' : listLocation.name}
				data.append(datacenter)
				node = {'country' : 'null', 'city' : region, 'datacenter' : data}

				nodelocations.append(node)
			
		nodesProvider = json.dumps(nodelocations)

	if provider == "EC2":
		pass
		accessId = driverUno
		secretKey = driverDos
		region = driverTres
		driverCuatro = driverCuatro
		driver = EC2NodeDriver(accessId, secretKey)

		listRegions = driver.list_regions()

	#	print listRegions

		nodelocations = []

		for listRegion in listRegions:
			region = listRegion

			if region == 'ap-south-1':
				pass
				region = 'ap-southeast-1'
			if region == 'us-east-2':
				pass
				region = 'us-east-1'
			if region == 'cn-north-1':
				pass
				region = 'us-east-1'
			if region == 'ca-central-1':
				pass
				region = 'us-east-1'
			if region == 'ap-northeast-2':
				pass
				region = 'ap-northeast-1'
			if region == 'us-gov-west-1':
				pass
				region = 'us-east-1'
			if region == 'eu-central-1':
				pass
				region = 'eu-west-1'
			if region == 'eu-west-2':
				pass
				region = 'eu-west-1'

			driverLocation = EC2NodeDriver(accessId, secretKey, None, None, None, region, None)

			listLocations = driverLocation.list_locations()

	#		print region

	#		print listLocations
			datacenterArray = []
			for listLocation in listLocations:
				flag = False
				for nodelocation in nodelocations:
					if 'country' in nodelocation:
						if nodelocation['country'] == listLocation.country:
							datacenter = {'id' : listLocation.name, 'name' : listLocation.name}
							datacenterArray.append(datacenter)
							flag = True
				if flag != True:
					datacenter = {'id' : listLocation.name, 'name' : listLocation.name}
					datacenterArray.append(datacenter)
					regionName = getRegionName.regionsAmazon(listRegion)
					if regionName != 'null':
						regionID = {'country' : listLocation.country, 'city' : regionName, 'datacenter' : datacenterArray}
						nodelocations.append(regionID)
							
		nodesProvider = json.dumps(nodelocations)


	if provider == "Azure":
		pass
		tenantId = driverUno
		subscriptionId = driverDos
		applicationId = driverTres
		keyPaswd = driverCuatro
		driver = AzureNodeDriver(tenantId,subscriptionId,applicationId,keyPaswd)

		listLocations = driver.list_locations()

		nodelocations = []	
		for listLocation in listLocations:
			data = []
			flag = False
			country = listLocation.country

			if country is not None:
				pass
				matches = country.partition(',')

				
				if matches[1] == ',':

					dos = matches[2]
					country = dos[1:len(dos)]
					city = matches[0]

					for nodelocation in nodelocations:
						if nodelocation['city'] == city:
							datacenter = {'id' : listLocation.id, 'name' : listLocation.name}
							nodelocation['datacenter'].append(datacenter)
							flag = True
					if flag != True:			
						datacenter = {'id' : listLocation.id, 'name' : listLocation.name}
						data.append(datacenter)
						node = {'country' : country, 'city' : city, 'datacenter' : data}
						nodelocations.append(node)
				else:
					
					city = 'null'

					datacenter = {'id' : listLocation.id, 'name' : listLocation.name}
					data.append(datacenter)
					node = {'country' : country, 'city' : city, 'datacenter' : data}
					nodelocations.append(node)
			else:

				city = getRegionName.regionsAzure(listLocation.name)

				country = 'null'

				datacenter = {'id' : listLocation.id, 'name' : listLocation.name}	
				data.append(datacenter)	



				node = {'country' : country, 'city' : city, 'datacenter' : data}

				nodelocations.append(node)

		nodesProvider = json.dumps(nodelocations)
	if provider == "Linode":
		pass
		apiKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		driver = DigitalOceanNodeDriver(apiKey)

		listLocations = driver.list_locations()

		nodesProvider = listLocations
	return nodesProvider