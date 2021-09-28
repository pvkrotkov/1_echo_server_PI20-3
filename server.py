import socket
import errno
import sys
import csv
import hashlib

ADDR = '127.0.0.1'
PORT = 9090
log_file = open('log.txt', 'w')

def log(*args):
	print(*args)
	global log_file
	log_file.write(*args)
	log_file.write('\n')

def is_port_in_use(PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.bind(('127.0.0.1', PORT)) == 0

def find_user_by_ip(addr):
	with open('users.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=';')
		for row in reader:
			if (row['ip'] == addr):
				return row['name']
		return False

def is_password_correct(addr, pswd):
	with open('users.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=';')
		for row in reader:
			if row['ip'] == addr:
				return pswd == row['pswd']
		return False

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
		print('Порт занят.')
		PORT += 1
		print(f'Новый порт {PORT}, {type(PORT)}')
	sock.bind((ADDR, PORT))
	log(f'Начало прослушивания порта №{PORT}...')
	sock.listen(2)
except socket.error as e:
	print('Порт занят.', e)
	log('Невозможно запустить сервер!')
	sys.exit()


conn, addr = sock.accept()
log('Подключение клиента...')
conn.recv(1024)
if not find_user_by_ip(addr[0]):
	conn.send('Пожалуйста, представьтесь: '.encode())
	name = conn.recv(1024).decode()
	conn.send('Введите пароль: '.encode())
	pswd = hashlib.md5(conn.recv(1024)).hexdigest()
	with open('users.csv', 'a') as csvfile:
		writer = csv.DictWriter(csvfile, delimiter=';', fieldnames = ['ip', 'name', 'pswd'])
		writer.writerow({'ip': addr[0], 'name': name, 'pswd':pswd})


conn.send(f'Добро пожаловать, {find_user_by_ip(addr[0])}!\n'.encode())
conn.send('Введите пароль для входа: '.encode())
pswd = hashlib.md5(conn.recv(1024)).hexdigest()
if not is_password_correct(addr[0], pswd):
	conn.send('Неверный пароль!'.encode())
	conn.close()
log(f'Подключен пользователь {str(addr)}')

msg = ''
conn.send('Подключение установлено'.encode())
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
