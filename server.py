import socket

sock = socket.socket()
print('Запуск клиента...')
sock.bind(('127.0.0.1', 9091))
print('Начало прослушивания порта...')
sock.listen(1)
conn, addr = sock.accept()
print('Подключение клиента...')
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	print('Приём данных от клиента...')
	if not data:
		break
	msg += data.decode() + '\n'
	print('Отправка данных клиенту...')
	conn.send(data)

print(msg)

conn.close()
print('Остановка сервера.')

