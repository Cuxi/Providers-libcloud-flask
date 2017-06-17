#!/usr/bin/python
import json
import sys
import os
import re
import getRegionName	
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.ec2 import BaseEC2NodeDriver, EC2NodeDriver

def checkStatus(driver,ide,types):
	pass
	i = 0
	j = 0
	while i != 1:
		idsNodes = driver.list_nodes()
		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == ide:
				pass
				idNod = idNodes
				
		if idNod.state != types:
			pass
			i = 0
		if idNod.state == types:
			pass
			i = idNod
			break
	return i