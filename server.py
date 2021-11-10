import socket

UDP_MAX_SIZE = 65535

def listen(host = '127.0.0.1', port = 3000):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	s.bind((host, port)) #прослушивание по указанному хосту и порту
	print(f'Listening at {host}:{port}')

	members = []
	while True:
		msg, addr = s.recvfrom(UDP_MAX_SIZE)

		if addr not in members:
			members.append(addr) #добавляем пользователя в список участников

		if not msg:
			continue

		client_id = addr[1] #в качестве client_id используем порт
		if msg.decode('ascii') == '__join':
			print(f'Client {client_id} joined chat')
			continue

		msg = f'client {client_id}: {msg.decode("ascii")}'
		for member in members:
			if member == addr:
				continue
			s.sendto(msg.encode('ascii'), member)

if __name__ == "__main__":
	listen()


