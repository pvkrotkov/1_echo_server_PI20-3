import socket
import sys
import threading
import time

BUFFERSIZE = 1024
ADDR = '127.0.0.1'
PORT = 9090
SERVER = (ADDR, PORT)
USER_PORT = 10090

def is_port_in_use(PORT):
	try:
		socket.socket(socket.AF_INET, socket.SOCK_DGRAM).bind((ADDR, PORT))
		socket.socket().close()
	except socket.error as e:
		return True
	else:
		return False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
request = input('Введите адрес и порт для подключения через пробел.  \n'\
                'Нажмите Enter, чтобы использовать значение по умолчанию:\n')
if request:
    try:
        ADDR, USER_PORT = request.split()
        PORT = int(USER_PORT)
    except:
        print('Введены некорректные данные!')
        sys.exit()

try:
    while is_port_in_use(USER_PORT):
        USER_PORT += 1
    print(f'Порт клиента - {USER_PORT}')
    sock.bind((ADDR, USER_PORT))
    print('Соединение с сервером...')
except:
    print('Невозможно подключиться!')
    sys.exit()


msg = f'.{ADDR}'
sock.sendto(msg.encode(), SERVER)
while True:
        data = sock.recv(BUFFERSIZE).decode()
        print(data, '\n')
        if data == 'Подключение установлено.':
                break
        msg = input('_  ')
        sock.sendto(msg.encode(), SERVER)

while msg != 'exit':

    msg = input('текст сообщения>: ')
    msg = '<пустое сообщение>' if not msg else msg
    sock.sendto(msg.encode(), SERVER)

    data = sock.recv(BUFFERSIZE)
    print(data.decode() + '\n')

sock.close()
print('Разрыв соединения с сервером.')
