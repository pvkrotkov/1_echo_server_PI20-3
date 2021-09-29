from time import sleep
import socket

sock = socket.socket()
try:
    sock.connect(('localhost', 9090))
    print('Подключение к серверу')
    while True:
        text = input('Ввод данных: ')
        try:
            sock.send(text.encode())
            print('Отправка данных серверу')
            try:
                data = sock.recv(1024)
                print('Получение данных от сервера')
                if data.decode()=='exit':
                    sock.close()
                    print('Соединение с сервером разорвано')
                    break
            except:
                print('Ошибка при получении данных от сервера')
                break
        except:
            print('Ошибка при отправке данных')
            break
except:
    print('Ошибка при соединении с сервером')



