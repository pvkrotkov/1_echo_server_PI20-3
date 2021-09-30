import socket

sock = socket.socket()
sock.connect(('localhost', 9092))


while True:
    q = input()

    if q == 'exit':
        break
    x = bytes(q, encoding='utf-8')

    sock.send(x)
    data = sock.recv(1024)
    print(data)

sock.close()
