import socket
import time


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5001  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    hora_atual = client_socket.recv(1024).decode()
    print(hora_atual)

    while True:

        message = "0/12:35"
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal
        time.sleep(10)




    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()