#!/usr/bin/python
from flask import Flask
from flask import jsonify, request
from flask_restful import reqparse, abort, Api, Resource
import getAllNodesFunction, getLocationsFunction, getNodeFunction

app = Flask(__name__)
api = Api(app)



class GetAllNodes(Resource):
	def post(self):
	 	try:
	 		parser = reqparse.RequestParser()
			parser.add_argument('provider', type = str)
			parser.add_argument('driverUno', type = str)
			parser.add_argument('driverDos', type = str)
			parser.add_argument('driverTres', type = str)
			parser.add_argument('driverCuatro', type = str)
	 		idsNodes = []
	 		args = parser.parse_args()
	 		provider = args['provider']
	 		driverUno = args['driverUno']
	 		driverDos = args['driverDos']
 			driverTres = args['driverTres']
 			driverCuatro = args['driverCuatro']

 			nodes = getAllNodesFunction.getAllNodes(provider,driverUno,driverDos,driverTres,driverCuatro)

	 		idsNodes.append(nodes)
	 		return idsNodes

	 	except Exception as e:
	 		return {'error': str(e)}
class GetLocations(Resource):
	def post(self):
	 	try:
	 		parser = reqparse.RequestParser()
			parser.add_argument('provider', type = str)
			parser.add_argument('driverUno', type = str)
			parser.add_argument('driverDos', type = str)
			parser.add_argument('driverTres', type = str)
			parser.add_argument('driverCuatro', type = str)
	 		idsNodes = []
	 		args = parser.parse_args()
	 		provider = args['provider']
	 		driverUno = args['driverUno']
	 		driverDos = args['driverDos']
 			driverTres = args['driverTres']
 			driverCuatro = args['driverCuatro']

 			nodes = getLocationsFunction.getLocations(provider,driverUno,driverDos,driverTres,driverCuatro)

	 		idsNodes.append(nodes)
	 		return idsNodes

	 	except Exception as e:
	 		return {'error': str(e)}

class GetNode(Resource):
	def post(self):
	 	try:
	 		parser = reqparse.RequestParser()
			parser.add_argument('provider', type = str)
			parser.add_argument('driverUno', type = str)
			parser.add_argument('driverDos', type = str)
			parser.add_argument('driverTres', type = str)
			parser.add_argument('driverCuatro', type = str)
			parser.add_argument('nodeId', type = str)
	 		idsNodes = []
	 		args = parser.parse_args()
	 		provider = args['provider']
	 		driverUno = args['driverUno']
	 		driverDos = args['driverDos']
 			driverTres = args['driverTres']
 			driverCuatro = args['driverCuatro']
 			nodeId = args['nodeId']

 			nodes = getNodeFunction.getNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

	 		idsNodes.append(nodes)
	 		return idsNodes

	 	except Exception as e:
	 		return {'error': str(e)}


api.add_resource(GetAllNodes, '/GetAllNodes')
api.add_resource(GetNode, '/GetNode')
api.add_resource(GetLocations, '/GetLocations')

if __name__ == '__main__':
    app.run(port=5003,debug=True)