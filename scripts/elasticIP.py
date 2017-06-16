#!/usr/bin/python
import json
import sys
import os
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.ec2 import EC2NodeDriver


def setElasticIP(driver,ide):
	idsNodes = driver.list_nodes()

	for idNodes in idsNodes:
		#print idsNodes
		if idNodes.id == ide:
			pass
			idNod = idNodes

	elastic_ip = driver.ex_allocate_address()

	return driver.ex_associate_address_with_node(idNod, elastic_ip)