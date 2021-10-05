import socket

sock = socket.socket()
sock.connect(('localhost', 1991))
name = input("Enter your name: ")
sock.send(name.encode())
msg = ''
while msg != "exit":
	msg = input('You: ')
	sock.send(msg.encode())
	data = sock.recv(1024)
	print(data.decode())
sock.close()
