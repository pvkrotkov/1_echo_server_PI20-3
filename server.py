import socket

sock = socket.socket()
sock.bind(('',9093))
sock.listen(1)
conn = sock.accept()   
addr = sock.accept()    

while True:   
    data = conn.recv(1024)    
    if not data:
        break       
    conn.send(data.upper())
sock.close()
