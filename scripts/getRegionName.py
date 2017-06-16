#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import re
def regionsAmazon(x):
	
	if x == 'us-east-1':
		pass
		region = 'US East(N. Virginia)'
	if x == 'us-east-2':
		pass
		region = 'null'
	if x == 'us-west-1':
		pass
		region = 'US West(N.California)'
	if x == 'us-west-2':
		pass
		region = 'US West(Oregon)'
	if x == 'ca-central-1':
		pass
		region = 'null'
	if x == 'eu-west-1':
		pass
		region = 'EU(Ireland)'
	if x == 'eu-central-1':
		pass
		region = 'EU (Frankfurt)'
	if x == 'eu-west-2':
		pass
		region = 'null'
	if x == 'ap-northeast-1':
		pass
		region = 'Asia Pacific(Tokyo)'
	if x == 'ap-northeast-2':
		pass
		region = 'null'
	if x == 'ap-southeast-1':
		pass
		region = 'Asia Pacific (Singapore)'
	if x == 'ap-southeast-2':
		pass
		region = 'Asia Pacific(Sydney)'
	if x == 'ap-south-1':
		pass
		region = 'null'
	if x == 'sa-east-1':
		pass
		region = 'South America(Sao Paulo)'
	if x == 'us-gov-west-1':
		pass
		region = 'null'
	if x == 'cn-north-1':
		pass
		region = 'null'

	return region
def regionsAzure(x):

	matchName = re.search(r'[a-zA-Z]{0,}[ ]', x)
	matchNameDos = re.search(r'[ ][a-zA-Z]{0,}', x)

	matchUno = matchName.group()

	matchDos = matchNameDos.group()
	

	uno = x[0:len(matchUno)-1]
	dos = matchDos[1:len(matchDos)]

	region = uno + " " + dos

	return region