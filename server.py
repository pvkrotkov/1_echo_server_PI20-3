import socket

print('Идет запуск сервера')
sock = socket.socket()
sock.bind(('', 9099))
print('Начало прослушивания порта')
sock.listen(0)
conn, addr = sock.accept()
print('Идет подключение пользователя')
print(addr)

msg = ''


while msg!='exit':
    data = conn.recv(1024)
    msg = data.decode()
    print('Идет получение данных клиента:')
    print(msg)
    conn.send(data)


conn.close()
print('Идет остановка сервера')
