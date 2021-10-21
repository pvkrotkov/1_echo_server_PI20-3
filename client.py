import socket

sock = socket.socket()
sock.setblocking(True)
sock.connect(('localhost', 4957))
print('Connecting server')
message = ''
while message != 'exit':
    message = input('Your message: ')
    sock.send(message.encode())
    data = sock.recv(1024)
    print(f'Sent message "{data.decode()}" to the server')
sock.close()
print('Stopping')
