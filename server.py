import socket

print('Запуск сервера')
sock = socket.socket()
sock.bind(('', 9099))
sock.listen(0)
conn, addr = sock.accept()
print('Идет подключение пользователя')
print("Пользователь ", addr, " подключен")

msg = ''


while msg!='exit':
    data = conn.recv(1024)
    msg = data.decode()
    print('Получены данные клиента:', addr)
    print(msg)
    conn.send(data)


conn.close()
print('Идет остановка сервера')
