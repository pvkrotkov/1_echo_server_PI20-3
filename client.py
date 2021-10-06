import socket
import sys
import time

BUFFERSIZE = 1024
ADDR = '127.0.0.1'
PORT = 9090
SERVER = (ADDR, PORT)
USER_PORT = 10092

# функция проверки занятости порта
def is_port_in_use(PORT):
	try:
		socket.socket(socket.AF_INET, socket.SOCK_DGRAM).bind((ADDR, PORT))
		socket.socket().close()
	except socket.error as e:
		return True
	else:
		return False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # инициализация UDP-сокета
request = input('Введите адрес и порт для подключения через пробел.  \n'\
                'Нажмите Enter, чтобы использовать значение по умолчанию:\n')
if request:
    try:
        ADDR, USER_PORT = request.split() # назначаем адрес и порт при пользовательском вводе
        PORT = int(USER_PORT)
    except:
        print('Введены некорректные данные!')
        sys.exit()

try:
    while is_port_in_use(USER_PORT):
        USER_PORT += 1
    print(f'Порт клиента - {USER_PORT}')
    sock.bind((ADDR, USER_PORT)) # присваиваем каждому клиенту уникальный порт
    print('Соединение с сервером...')
except:
    print('Невозможно подключиться!')
    sys.exit()


msg = f'.{ADDR}' # отправляем стартовое сообщение на сервер - оно начинается с точки
sock.sendto(msg.encode(), SERVER)
while True: # цикл авторизации на сервере
	data, addr = sock.recvfrom(BUFFERSIZE)
	data = data.decode()
	print(data, '\n')
	if data == 'Подключение установлено.': # при получении сообщения с таким текстом считаем пользователя залогиненным
		break
	msg = input('_ ')
	sock.sendto(msg.encode(), SERVER)

# основной цикл отправки сообщения на сервер
while msg != 'exit':

    msg = input('текст сообщения>: ')
    msg = '<пустое сообщение>' if not msg else msg # вместо '' отправляем текст <пустое сообщение>
    sock.sendto(msg.encode(), SERVER)

    data, addr = sock.recvfrom(BUFFERSIZE)
    print(data.decode() + '\n')

sock.close()
print('Разрыв соединения с сервером.')
