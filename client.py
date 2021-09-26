import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('', 9091))
print('Соединение с сервером...')


msg = input()
while msg != 'exit':
    sock.send(msg.encode())
    print('Отправка данных серверу...')

    data = sock.recv(1024)
    print('Приём данных от сервера...')

    print(data.decode())
    msg = input()

sock.close()
print('Разрыв соединения с сервером.')
