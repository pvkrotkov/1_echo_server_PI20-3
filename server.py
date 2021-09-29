import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
msg = ""

try:
    sock.connect(('localhost', 8080))
    print('Connected to server')
    while msg != "exit":
        msg = input('Input your message: ')
        sock.send(msg.encode())
        data = sock.recv(1024)
except:
    print('Connection error\nShutdown')

sock.close()
