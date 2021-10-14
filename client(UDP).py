import os
import threading
import socket
UDP_MAX_SIZE = 65535

def listen(sock: socket.socket):
    while True:
        msg = sock.recv(UDP_MAX_SIZE)
        print("\r\r" + msg.decode("ASCII") + "\n" + f"you: ", end="")

def connect(host: str = "127.0.0.1", port: int = 9093):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((host, port))
    threading.Thread(target=listen, args=(sock,), daemon=True).start()
    sock.send("__join".encode("ASCII"))
    while True:
        msg = input(f'you: ')
        sock.send(msg.encode("ASCII"))

if __name__ == "__main__":
    os.system("Clear")
    print("Welcome to chat!")
    connect()
