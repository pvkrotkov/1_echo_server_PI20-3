import socket
import sys

ADDR = '127.0.0.1'
PORT = 9090
log_file = open('log.txt', 'w')

def log(*args):
	print(*args)
	global log_file
	log_file.write(*args)
	log_file.write('\n')

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

sock = socket.socket()
log('Запуск сервера...')

request = input('Введите адрес и порт сервера.  \n'\
                'Нажмите Enter, чтобы использовать значение по умолчанию:\n')
if request:
    try:
        ADDR, PORT = request.split()
        PORT = int(PORT)
    except:
        log('Введены некорректные данные!')
        sys.exit()

try:
	while is_port_in_use(PORT):
		PORT += 1
	sock.bind((ADDR, PORT))
	log(f'Начало прослушивания порта №{PORT}...')
	sock.listen(2)
except:
	log('Невозможно запустить сервер!')
	sys.exit()


conn, addr = sock.accept()
log('Подключение клиента...')
log(str(addr))

msg = ''

while True:
	data = conn.recv(1024)
	log('Приём данных от клиента...')
	if not data:
		log('Данных нет. Прослушивание порта...')
		conn, addr = sock.accept()
	msg += data.decode() + '\n'
	log('Отправка клиенту: ')
	log(str(addr) + ' ' + data.decode())
	conn.send(data)

log(msg)

conn.close()
log('Остановка сервера.')
log_file.close()
