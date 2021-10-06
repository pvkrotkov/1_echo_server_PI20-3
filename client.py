import socket
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('10.4.54.7', 1443)


def read():
    while 1:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


name = input('Введите имя: ')

sock.sendto(('\n'+name + ' Connect to server'+ '\n' + 'you: ').encode('utf-8'), server)
pot = threading.Thread(target=read)
pot.start()

msg = ''
while msg != 'exit':
    msg = input('you:\n')
    sock.sendto(('\n'+'['+name+']' + msg + '\n' + 'you: ').encode('utf-8'), server)

sock.close()
