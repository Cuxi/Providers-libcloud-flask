#!/usr/bin/python
import json
import sys
import os
import re
import getRegionName	
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.ec2 import BaseEC2NodeDriver, EC2NodeDriver

def checkStatus(driver,ide):
	pass
	i = 0
	while i != 1:
		idsNodes = driver.list_nodes()
		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == ide:
				pass
				idNod = idNodes
				print idNod
				
		if idNod.state != 'running':
			pass
			i = 0
		if idNod.state == 'running':
			pass
			print '1'
			i = 1
	return 1