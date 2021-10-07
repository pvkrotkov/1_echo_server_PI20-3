from socket import *

clients = []

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 1337))

print("Сервер включен")
cl = False

while not cl:
    try:
        data, addr = sock.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)
            print(addr[1],'присоединился')

        for client in clients:
            if addr != client:
                sock.sendto(data,client)
    except:
        print("Сервер приостановлен")
        cl = True

sock.close()
