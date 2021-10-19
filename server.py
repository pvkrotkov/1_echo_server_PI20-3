import socket

sock = socket.socket()

print('The server has launched!')
sock.bind(('', 9090))
sock.listen()
print('The server is listening on port 9090!')
conn, addr = sock.accept()
print('Client has connected with address {}'.format(addr[0]+':'+str(addr[1])))

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		break
	if data.decode() == 'exit':
		print('Client has disconnected!')
		break
	print('Recieved data from client!')
	msg += data.decode()
	print('Sending data to client!')
	conn.send(data.upper())

conn.close()
print('The server has stopped!')
