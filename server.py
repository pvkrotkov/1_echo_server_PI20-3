import socket

print('Launching the server...')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
users = []
try:
    s.bind(('', 9090))
    print('Success!\nWaiting...')
    while True:
        data, addr = s.recvfrom(1024)
        if addr not in users:
            print('New user has connected. Address:', addr)
            users.append(addr)
        print(data)
        for i in users:
            if i != addr:
                s.sendto(data, i)

except:
    print('Launching error')
