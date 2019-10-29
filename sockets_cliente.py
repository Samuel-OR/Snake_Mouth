import socket
ip = 'localhost'
port = 7000
addr = ((ip,port)) #define a tupla de endereco
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que eh TCP/IP
client_socket.connect(addr) #realiza a conexao


class ClientSocket():
	def __init__(self):
		self.ip = 'localhost'
		self.port = 7000
		self.addr = ((ip,port)) #define a tupla de endereco
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que eh TCP/IP
		self.client_socket.connect(addr) #realiza a conexao

	def enviar_dados(self,conteudo):
		self.client_socket.send(conteudo.encode())
		if self.client_socket.recv(1024).decode() == "ok":
			return True
		else:
			return False
			 