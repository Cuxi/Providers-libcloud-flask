#!/usr/bin/python
from flask import Flask
from flask import jsonify, request
from flask_restful import reqparse, abort, Api, Resource
import getAllNodesFunction, getLocationsFunction, getNodeFunction
import deleteNodeFunction
import createNodeFuntion
import resizeNodeFunction
import shutdownNodeFunction, startNodeFunction, rebootNodeFunction

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

class DeleteNode(Resource):
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

 			nodes = deleteNodeFunction.deleteNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

	 		idsNodes.append(nodes)
	 		return idsNodes

	 	except Exception as e:
	 		return {'error': str(e)}

class CreateNode(Resource):
	def post(self):
	 	try:
	 		parser = reqparse.RequestParser()
			parser.add_argument('provider', type = str)
			parser.add_argument('driverUno', type = str)
			parser.add_argument('driverDos', type = str)
			parser.add_argument('driverTres', type = str)
			parser.add_argument('driverCuatro', type = str)
			parser.add_argument('name', type = str)
			parser.add_argument('size', type = str)
			parser.add_argument('image', type = str)
			parser.add_argument('location', type = str)
			parser.add_argument('ex_network', type = str)
	 		idsNodes = []
	 		args = parser.parse_args()
	 		provider = args['provider']
	 		driverUno = args['driverUno']
	 		driverDos = args['driverDos']
 			driverTres = args['driverTres']
 			driverCuatro = args['driverCuatro']
 			name = args['name']
 			size = args['size']
 			image = args['image']
 			location = args['location']
 			ex_network = args['ex_network']

 			nodes = createNodeFuntion.createNode(provider,driverUno,driverDos,driverTres,driverCuatro,name,size,image,location,ex_network)

	 		idsNodes.append(nodes)
	 		return idsNodes

	 	except Exception as e:
	 		return {'error': str(e)}

class ResizeNode(Resource):
	def post(self):
	 	try:
	 		parser = reqparse.RequestParser()
			parser.add_argument('provider', type = str)
			parser.add_argument('driverUno', type = str)
			parser.add_argument('driverDos', type = str)
			parser.add_argument('driverTres', type = str)
			parser.add_argument('driverCuatro', type = str)
			parser.add_argument('size', type = str)
			parser.add_argument('nodeId', type = str)
			idsNodes = []
	 		args = parser.parse_args()
	 		provider = args['provider']
	 		driverUno = args['driverUno']
	 		driverDos = args['driverDos']
 			driverTres = args['driverTres']
 			driverCuatro = args['driverCuatro']
 			size = args['size']
 			nodeId = args['nodeId']
 			
 			nodes = resizeNodeFunction.resizeNode(provider,driverUno,driverDos,driverTres,driverCuatro,size,nodeId)

	 		idsNodes.append(nodes)
	 		return idsNodes

	 	except Exception as e:
	 		return {'error': str(e)}

class ShutdownNode(Resource):
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

 			nodes = shutdownNodeFunction.shutdownNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

	 		idsNodes.append(nodes)
	 		return idsNodes

	 	except Exception as e:
	 		return {'error': str(e)}

class StartNode(Resource):
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

 			nodes = startNodeFunction.startNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

	 		idsNodes.append(nodes)
	 		return idsNodes

	 	except Exception as e:
	 		return {'error': str(e)}

class RebootNode(Resource):
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

 			nodes = rebootNodeFunction.rebootNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId)

	 		idsNodes.append(nodes)
	 		return idsNodes

	 	except Exception as e:
	 		return {'error': str(e)}


api.add_resource(GetAllNodes, '/GetAllNodes')
api.add_resource(GetNode, '/GetNode')
api.add_resource(GetLocations, '/GetLocations')
api.add_resource(CreateNode, '/CreateNode')
api.add_resource(DeleteNode, '/DeleteNode')
api.add_resource(ResizeNode, '/ResizeNode')
api.add_resource(ShutdownNode, '/ShutdownNode')
api.add_resource(StartNode, '/StartNode')
api.add_resource(RebootNode, '/RebootNode')

if __name__ == '__main__':
    app.run(port=5003,debug=True)
