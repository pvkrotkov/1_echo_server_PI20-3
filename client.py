import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9091))
print('connected to server.')
while True:
    msg = input('message: ')
    if msg=='exit':
        sock.send(msg.encode())
        data = sock.recv(1024)
        print(data.decode())
        sock.close()
        break
    else:
        sock.send(msg.encode())
    
        data = sock.recv(1024)

    print('server: ',data.decode())