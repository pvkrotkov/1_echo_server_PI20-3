import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9091))

message = ''
msg = input('Enter text: ')
while msg!='exit':
	message+=msg
	message+=' '
	msg = input('Enter text: ')

sock.send(message.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
