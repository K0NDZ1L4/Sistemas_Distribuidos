import socket
from clock import get_time


def client():
    HOST = "localhost"
    PORT = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    while True:
        date_time = get_time()
        data_send = str.encode(date_time)

        sock.sendall(data_send)
        data_recv = sock.recv(1024).decode()

        if data_recv == "-1":
            break

        else:
            print("Msg recv from server: " + data_recv)
