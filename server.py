import socket

sock = socket.socket()
msg = ''
print('Launching the server...')
try:
    sock.bind(('', 8080))
    print('Success')
    sock.listen()
    conn, addr = sock.accept()
    print('The client is connected')
    print('Address: ' + str(addr))
    while msg != "exit":
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        conn.send(data)
        print('Message: ' + str(msg))
except:
    print('Launch error')
