import socket
UPD_MAX_SIZE = 65535

def listen(host:str = "127.0.0.1", port: int = 9093):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((host,port))
    print(f'listening at {host}:{port}')
    members =[]
    while True:
        msg = sock.recvfrom(UPD_MAX_SIZE)
        addr = sock.recvfrom(UPD_MAX_SIZE)
        if addr not in members:
            members.append(addr)
        if not msg:
            continue
        client_id = addr[1]
        if msg.decode('ASCII') == "__join":
            print(f'client{client_id} joined')
            continue
        msg =f'client{client_id}: {msg.decode("ASCII")}'
        for member in members:
            if member ==addr:
                continue

            sock.sendto(msg.encode("ASCII"), member)
if __name__== "__main__":
    listen()
