from socket import *
import threading


sock = socket(AF_INET, SOCK_DGRAM)
server = ('localhost', 1337)


def read():
    while 1:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


name = input('Введите имя: ')

sock.sendto(('\n'+name + ' присоединился к серверу'+ '\n' + 'Вы: ').encode('utf-8'), server)
pot = threading.Thread(target=read)
pot.start()

msg = ''
while msg != 'exit':
    msg = input('Вы: ')
    sock.sendto(('\n' + name + ': ' + msg + '\n' + 'Вы: ').encode('utf-8'), server)

sock.close()
