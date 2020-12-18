import socket
from threading import Thread


client_socket = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM

)
client_socket.connect(("127.0.0.1", 1234))


def client_listen_ability():
    while True:
        data = client_socket.recv(4096)
        if data:
            print(data.decode("utf-8"))


def event_loop():
    name = input("What is your name?: ")
    listen = Thread(target=client_listen_ability)
    listen.start()

    while True:
        c = f"{name} says:"
        g = input()
        client_socket.send(f"{c+g}".encode())


if __name__ == '__main__':
    event_loop()
