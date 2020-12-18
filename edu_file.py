import socket
import selectors


selector = selectors.DefaultSelector()
users = []


def send_all(data, usr_socket):
    for u in users:
        if usr_socket != u:
            u.send(data)


def server():
    server_socket = socket.socket(

        socket.AF_INET,
        socket.SOCK_STREAM

        )

    server_socket.bind(("127.0.0.1", 1234))
    server_socket.listen()
    selector.register(server_socket, selectors.EVENT_READ, accept_socket)


def accept_socket(server_socket):
    usr_socket, addr = server_socket.accept()
    print(f"User {addr} is connected")
    users.append(usr_socket)
    usr_socket.send("You are connected".encode())
    selector.register(usr_socket, selectors.EVENT_READ, send_socket)


def send_socket(usr_socket):
    data = usr_socket.recv(4096)
    print(data.decode("utf-8"))
    send_all(data, usr_socket)


def event_loop():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
