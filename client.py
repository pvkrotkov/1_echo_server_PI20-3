import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))
print('соединение с сервером')
msg=''
while (msg!='exit'):
    print('Введите данные:')
    msg = input()
    print('Отправляю данные на сервер')
    sock.send(msg.encode())
    data = sock.recv(1024)

sock.close()
print('отключение от сервера')
print(data.decode())
