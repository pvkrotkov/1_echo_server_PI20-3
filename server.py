import sys
import time
import socket

sock = socket.socket()
try:
    sock.bind(('localhost', 9090))
    print('Сервер запущен')
    try:
        sock.listen(1)
        print('Прослушивание парта запущено')
        try:
            client, address = sock.accept()
            print('Подключение клиента')
            while True:
                text = ''
                try:
                    data = client.recv(1024)
                    print('Получение данных от клиента')
                    if not data:
                        break
                    text += data.decode()
                    try:
                        client.send(data)
                        print('Получено сообщение: ' + text)
                        print('Отправка данных клиенту')
                        if text == 'exit':
                            break
                            client.close()
                    except:
                        print('Ошибка при отправке данных клиенту')
                except:
                    print('Ошибка при получении данных от клиента')
                    break
        except:
            print('Ошибка при подключении клиента')
    except:
        print('Ошибка при прослушивании порта')
except:
    print('Ошибка запуска сервера')


print('Клиент отключен')
print('Сервер остановлен')