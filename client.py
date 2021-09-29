import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

#msg = input()
msg = ""
while True:
    msg = input()
    sock.send(msg.encode())
    data = sock.recv(1024)
    if msg == 'exit':
        break


sock.close()

print(data.decode())
