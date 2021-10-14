import socket
from time import sleep
import threading
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('127.0.0.1', 9090)
nickname = input('Input your nickname: ')


def getData():
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


while True:
    msg = input()
    if msg == "EXIT":
        print('You were disconnected')
        sock.close()
    else:
        sock.sendto((nickname + ': ' + msg).encode('utf-8'), server)
        thread = threading.Thread(target=getData)
        thread.start()

