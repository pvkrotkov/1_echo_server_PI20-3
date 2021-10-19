import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))
print("Connected to the server!")
while True:
	msg = input('Input message: ')
	if msg=='exit':
		sock.send(msg.encode())
		sock.close()
		print("Connection is closed!")
		break
	else:
		print("Sending message to the server...")
		sock.send(msg.encode())
		data = sock.recv(1024)
		print("Recieved from the server:", data.decode())
