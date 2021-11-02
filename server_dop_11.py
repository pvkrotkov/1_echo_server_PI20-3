import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
#print(f'Сервер: {host}')
server.bind(('', 9093))
server.listen(5)

print ('exit для выхода с сервера')

clients = list() #Список клиентов
end = list() #Клиенты, которые создали потоки

#Блокировка ожидания подключения клиента, возврата объекта подключения и адреса косвенного объекта
def accept():
    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f'сервер подключен через {addr}: текущее количество подключений: -- {len (clients)}', end = '')


def recv_data(client):
    while True:
        #Принимаем информацию от клиента
        try:
            indata = client.recv(1024)
        except:
            clients.remove(client)
            end.remove(client)
            print(f'Сервер отключен: текущее количество подключений: -- {len (clients)}', end = '')
            break
        print(indata.decode('utf-8'))
        for clien in clients:
            # Перенаправить информацию от клиента и отправить ее другим клиентам
            if clien != client:
                clien.send(indata)

def outdatas():
    while True:
        print('')
        outdata = input('')
        print()
        if outdata == 'exit' or outdata == 'Exit':
            break
            print('Отправить всем: % s'% outdata)
         # Отправлять информацию каждому клиенту
        for client in clients:
            client.send (f"Сервер: {outdata}". encode ('utf-8)'))


def indatas():
    while True:
         #Выполните цикл подключенных клиентов и создайте соответствующий поток
        for clien in clients:
             # Если поток уже существует, пропустить
            if clien in end:
                continue
            index = threading.Thread(target = recv_data,args = (clien,))
            index.start()
            end.append(clien)


 #Создать многопоточность

t1 = threading.Thread(target = indatas,name = 'input') #Создать получающую информацию, объект потока
t2 = threading.Thread(target = outdatas, name= 'out') #Создать отправляемое сообщение, объект потока
t1.start()
t2.start()

 #Ожидание подключения клиента, объект потока
t3 = threading.Thread(target = accept(),name = 'accept')
t3.start()

t2.join()

 #выключение
for client in clients:
    client.close()
print ('сервер отключен')

