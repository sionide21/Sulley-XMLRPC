from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

def client (host, port):
	'''
		Instead of a client class, this is a function that 
		returns a SimpleXMLRPCServer
	'''
		return xmlrpclib.ServerProxy("http://%s:%d/" % (host,port))
		
class server:
	def __init__ (self, host, port):
		self.__server = SimpleXMLRPCServer((host, port))
		self.__server.register_instance(self)
	
	def serve_forever (self):
		self.__server.serve_forever()