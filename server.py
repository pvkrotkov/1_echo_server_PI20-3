import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('', 9090))
sock.listen(3)

print ('exit для выхода с сервера')
clients = list() #Список клиентов
end = list() #Клиенты, которые создали потоки

#то что было ко второму заданию
"""while True: 
	data = conn.recv(1024)
	if not data:
		break
	msg = data.decode()
	conn.send(data)
	print(msg)"""


def accept():
    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f'сервер подключен через {addr}: текущее количество подключений: -- {len (clients)}', end = '')

def recv_data(client):
    while True: #Принимаем информацию от клиента
        try:
            indata = client.recv(1024)
        except:
            clients.remove(client)
            end.remove(client)
            print(f'Сервер отключен: текущее количество подключений: -- {len (clients)}', end = '')
            break
        print(indata.decode('utf-8'))
        for cl in clients: # Перенаправить информацию от клиента и отправить ее другим клиентам
            if cl != client:
                cl.send(indata)

def vvod():
    while True:
        print('') #Ввод информации, которая будет предоставлена клиенту
        outdata = input('')
        print()
        if outdata == 'exit' or outdata == 'Exit':
            break
            print('Отправить всем: % s'% outdata)
        # Отправить информацию каждому клиенту
        for client in clients:
            client.send (f"Сервер: {outdata}". encode ('utf-8)'))
	
def priem():
    while True: #цикл подключенных клиентов и создайте соответствующий поток
        for clien in clients:
            # Если поток уже существует, пропустить
            if clien in end:
                continue
            index = threading.Thread(target = recv_data,args = (clien,))
            index.start()
            end.append(clien)
	
#Создать многопоточность
t1 = threading.Thread(target = priem,name = 'input') #объект потока. получает информацию
t2 = threading.Thread(target = vvod, name = 'out') #объект потока. отправляет информацию
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
