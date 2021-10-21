import socket

print('Running server')
sock = socket.socket()
sock.bind(('', 4957))
sock.listen(0)
connection, address = sock.accept()
print('Connecting user')
print(f'User {address} connected')
message = ''
while message != 'exit':
    data = connection.recv(1024)
    message = data.decode()
    print(f'Got {address} client\'s data')
    print(message)
    connection.send(data)
connection.close()
print('Stopping server')
