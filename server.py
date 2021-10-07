import socket


sock = socket.socket()
sock.bind(('', 11490)) 
sock.listen(1)  # прослушивание 
conn, addr = sock.accept() # принимет подключение
while True: 
    data = conn.recv(1024)  #получение данных от клиента(1024байт)
    print(data.decode())
    conn.send('server-echo'.encode())  # sending клиенту ответ

    if data.decode() == 'exit': 
        break
conn.close()
sock.close() 
