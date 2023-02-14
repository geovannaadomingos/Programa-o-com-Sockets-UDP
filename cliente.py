from socket import socket, AF_INET, SOCK_STREAM

myClientSocket = socket(AF_INET, SOCK_STREAM)
print(f'socket cliente criado')

myClientSocket.connect(('127.0.0.1', 9090))

while True:
    msg = input('>>')
    myClientSocket.send(msg.encode())
    data = myClientSocket.recv(2048)
    reply = data.encode()
    print(f'A resposta da solicitação foi {reply}')