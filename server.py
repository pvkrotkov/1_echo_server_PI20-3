import socket

clients = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 1443))

print("Server Started")
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
        print("\n[ Server Stopped ]")
        cl = True

sock.close()
