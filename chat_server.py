import socket

localIP = 'localhost'
localPort = 9095
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening\nWaiting for the first messege from client")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    messege = bytesAddressPair[0]
    print('messege from client -', messege.decode('utf8', 'strict'))
    address = bytesAddressPair[1]
    if messege == b'exit':
        break
    b = bytes(input('your messege - '), encoding='utf-8')
    if b == b'exit':
        UDPServerSocket.sendto(b, address)
        break
    UDPServerSocket.sendto(b, address)

UDPServerSocket.close()
