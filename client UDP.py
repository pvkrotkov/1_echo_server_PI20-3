import socket
import threading
import os


UDP_max = 65535


def listen(sock: socket.socket):
    while True:
        text = sock.recv(UDP_max)
        print('\r\r' + text.decode('ascii') + '\n' + f'you: ', end='')


def connect(host: str = '127.0.0.1', port: int = 9080):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.connect((host, port))

    threading.Thread(target=listen, args=(sock,), daemon=True).start()

    sock.send('__join'.encode('ascii'))

    while True:
        text = input(f'you: ')
        sock.send(text.encode('ascii'))


if __name__ == '__main__':
    os.system('clear')
    print('Welcome to chat!')
    connect() 