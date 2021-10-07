import socket


sock = socket.socket() 
sock.setblocking(1)
sock.connect(('localhost', 11490)) 


sock.send('client joined'.encode())
while True:
    mes = (input('type: ')).encode()
    sock.send(mes)
    if mes.decode() == 'exit':
        break
data = sock.recv(1024)
print(data.decode())
sock.close()
