import socket


UPD_max = 65535

def listen(host:str = '127.0.0.1', port: int = 9080):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock.bind((host,port))
    print(f'listening at {host}:{port}')

    clients =[]

    while True:
        text, addr = sock.recvfrom(UPD_max)

        if addr not in clients:
            clients.append(addr)

        if not text:
            continue

        client_id = addr[1]
        if text.decode('ascii') == '__join':
            print(f'client{client_id} joined')
            continue

        text =f'client{client_id}: {text.decode("ascii")}'

        for client in clients:
            if client ==addr:
                continue

            sock.sendto(text.encode("ascii"), client)
            
if __name__== '__main__':
    listen()