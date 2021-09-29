import socket
import sys

ADDR = '127.0.0.1'
PORT = 9090
sock = socket.socket()
sock.setblocking(1)

request = input('Введите адрес и порт для подключения через пробел.  \n'\
                'Нажмите Enter, чтобы использовать значение по умолчанию:\n')
if request:
    try:
        ADDR, PORT = request.split()
        PORT = int(PORT)
    except:
        print('Введены некорректные данные!')
        sys.exit()

try:
    sock.connect((ADDR, PORT))
    print('Соединение с сервером...')
except:
    print('Невозможно подключиться!')
    sys.exit()


msg = f'IP: {ADDR}, PORT:{PORT}'
while msg != 'exit':
    sock.send(msg.encode())
    print('Отправка данных серверу...')

    data = sock.recv(1024)
    print('Приём данных от сервера...')

    print(data.decode() + '\n')
    msg = input()
    msg = '<пустое сообщение>' if not msg else msg

sock.close()
print('Разрыв соединения с сервером.')
