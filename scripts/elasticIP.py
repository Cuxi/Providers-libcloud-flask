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

	driver.ex_associate_address_with_node(idNod, elastic_ip)
	return elastic_ip

#Traceback (most recent call last):
#  File "./createNode.py", line 107, in <module>
#    elastic = elasticIP.setElasticIP(driver,node.id)
#  File "/var/www/html/elasticIP.py", line 19, in setElasticIP
#    elastic_ip = driver.ex_allocate_address()
#  File "/usr/lib/python2.7/dist-packages/libcloud/compute/drivers/ec2.py", line 4450, in ex_allocate_address
#    response = self.connection.request(self.path, params=params).object
#  File "/usr/lib/python2.7/dist-packages/libcloud/common/base.py", line 871, in request
#    response = responseCls(**kwargs)
#  File "/usr/lib/python2.7/dist-packages/libcloud/common/base.py", line 180, in __init__
#    headers=self.headers)
#libcloud.common.exceptions.BaseHTTPError: AddressLimitExceeded: The maximum number of addresses has been reached.