import socket

class Enviar(object):
	
	def __init__(self):
		self.host = "localhost"
		self.port = 7008
		self.address = (self.host, self.port)
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criar socket
		self.connection()

	def connection(self):
		self.client_socket.connect(self.address)

	def enviarDados(self, dados):
		self.client_socket.send(dados.encode())


