import socket

sock = socket.socket()
sock.bind(('localhost', 9098))
sock.listen(1)
conn, addr = sock.accept()
mes = ''

while True:
    data = conn.recv(1024)
    if not data:
        break
    mes = data.decode()
    conn.send(data.upper())
    print(mes)
sock.close()
