import socket

sock = socket.socket()
sock.connect(('localhost', 9098))

while True:
    a1 = input()
    if a1 == 'exit':
        break
    sock.send(a1.encode())

    data = sock.recv(1024)

    print(data)

sock.close()
