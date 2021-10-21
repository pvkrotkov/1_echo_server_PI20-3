import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.connect(('localhost', 9095))
print('client up\ntype the first messege')

while True:
    b = bytes(input('your messege - '), encoding='utf-8')
    if b == b"exit":
        sock.sendto(b, ('localhost', 9095))
        break
    sock.sendto(b, ('localhost', 9095))
    data = sock.recvfrom(1024)

    print('messege from server -', data[0].decode('utf-8'))
    if data[0] == b'exit':
        break

sock.close()
