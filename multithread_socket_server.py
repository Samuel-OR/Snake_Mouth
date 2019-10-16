
import BancoDeDados as BD
import socket, threading
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)


    def run(self):
        print ("Conectado de: ", clientAddress)
        msg = ''
        data = ''
        while True:
            data = self.csocket.recv(1024)
            break

        msg = data.decode()
        print("REceiver: ", msg)
        
        lista = msg.split(',')

        user= lista[0]
        password = lista[1]
        name = lista[1]

        cad = BD.login(user, password)
        cad = str(cad)

        BD.registerTeacher(email, password, name)

        print("Retorno:", cad)
        print ("from client", msg)
        self.csocket.send(cad.encode())
        

        print ("Client at ", clientAddress , " disconnected...")
if __name__ == '__main__':
    LOCALHOST = ''
    PORT = 7000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
