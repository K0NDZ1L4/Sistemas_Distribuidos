import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host = socket.gethostname()
port = 5001
ThreadCount = 0



try:
    ServerSideSocket.bind((host, port))
    ServerSideSocket.listen(5)
except socket.error as e:
    print(str(e))
print('Socket is listening..')


def multi_threaded_client(connection):
    connection.send(str.encode('Hora Atual: 12:00'))
    while True:
        data = connection.recv(2048).decode('utf-8')
        data = data.split("/")
        if data[0] == "0":
            response = 'responsavel'
        elif data[0] != "0":
            response = "nao responsavel"
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()


while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()