from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def HandleRequest(mClientSock, mClientAddr):
    data = clienteSock.recv(2048)
    req = data.decode()
    print(f'A solicitação feita pelo cliente foi {req}')
    rep = 'sei qualquer coisa'
    mClientSock.send(rep.encode())
    print(f'Mensagem enviada...')

#criação de um socket genérico
myServerSocket = socket(AF_INET, SOCK_STREAM)
print(f'socket criado')

#indicando um ip loopback
myServerSocket.bind(('127.0.0.1', 9090))
myServerSocket.listen()

while True:
    clienteSock, clienteAddr = myServerSocket.accept()
    print(f'O cliente {clienteAddr} enviou uma solicitação')
    Thread(target =HandleRequest, args=(clienteSock, clienteAddr))