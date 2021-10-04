import socket
import sys
import csv
import hashlib
import time

ADDR = '127.0.0.1'
BUFFERSIZE = 1024
PORT = 9090
log_file = open('log.txt', 'w')

def log(*args):
	print(*args)
	global log_file
	log_file.write(f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}] - ')
	log_file.write(*args)
	log_file.write('\n')

def is_port_in_use(PORT):
	try:
		socket.socket(socket.AF_INET, socket.SOCK_DGRAM).bind((ADDR, PORT))
		socket.socket().close()
	except socket.error as e:
		return True
	else:
		return False

def find_user_by_id(addr):
	with open('users.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=';')
		for row in reader:
			if (int(row['id']) == int(addr[1])):
				return row['name']
		return False

def is_password_correct(addr, pswd):
	with open('users.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=';')
		for row in reader:
			if (int(row['id']) == int(addr[1])):
				return pswd == row['pswd']
		return False


def greet_client(sock, addr):

	if not find_user_by_id(addr):
		sock.sendto('Пожалуйста, представьтесь: '.encode(), addr)
		name = sock.recvfrom(BUFFERSIZE)[0].decode()
		sock.sendto('Введите пароль: '.encode(), addr)
		pswd = hashlib.md5(sock.recv(BUFFERSIZE)).hexdigest()
		with open('users.csv', 'a') as csvfile:
			writer = csv.DictWriter(csvfile, delimiter=';', fieldnames = ['id', 'ip', 'name', 'pswd'])
			writer.writerow({'id': addr[1], 'ip': addr[0], 'name': name, 'pswd':pswd})
	else:
		sock.sendto(f'Добро пожаловать, {find_user_by_id(addr)}!\nВведите пароль для входа:\n'.encode(), addr)
		pswd = hashlib.md5(sock.recv(BUFFERSIZE)).hexdigest()
		while not is_password_correct(addr, pswd):
			sock.sendto('Неверный пароль!'.encode(), addr)
			pswd = hashlib.md5(sock.recv(BUFFERSIZE)).hexdigest()
	log(f'Подключен клиент {addr}')
	sock.sendto('Подключение установлено.'.encode(), addr)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
log('Запуск сервера.')
request = input('Введите адрес и порт сервера.  \n'\
                'Нажмите Enter, чтобы использовать значение по умолчанию:\n')
if request:
    try:
        ADDR, PORT = request.split()
        PORT = int(PORT)
    except:
        print('Введены некорректные данные!')
        sys.exit()

try:
	while is_port_in_use(PORT):
		print(f'Порт {PORT} занят.')
		PORT += 1
	sock.bind((ADDR, PORT))
	log(f'Начало прослушивания порта №{PORT}...')
except socket.error as e:
	print(e)
	log('Невозможно запустить сервер!')
	sys.exit()


msg = ''
users = []
while True:
	data, addr = sock.recvfrom(BUFFERSIZE)
	log('Получение пакета')
	data = data.decode()
	if data[0] == '.':
		log('Подключение клиента...')
		greet_client(sock, addr)
		users.append(addr)
		continue

	if not data:
		log('Данных нет. Прослушивание порта...')
		data, addr = sock.accept()

	itsatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	print(f'[{addr[0]}]=[{str(addr[1])}]=[{itsatime}]| {data}')

	for user in users:
		if user != addr:
			sock.sendto(f'[{find_user_by_id(addr)}]: {data}'.encode(), user)
			log(f'Отправка данных на {user}.')



sock.close()
log('Остановка сервера.')
log_file.close()
