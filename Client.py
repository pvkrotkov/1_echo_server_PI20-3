import socket

sock = socket.socket()
sock.connect(('localhost', 9094))

while True:

    a = input()
    if a == 'exit':
        break
    b = bytes(a, encoding='utf-8')

    sock.send(b)

    data = sock.recv(1024)

    print (data)

sock.close()
