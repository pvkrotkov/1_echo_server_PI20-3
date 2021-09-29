# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:37:18 2021

@author: okazm
"""

import socket
from time import sleep

msg=''

sock = socket.socket()
sock.bind(('', 9091))
sock.listen(1)
print('waiting for client...')
conn, addr = sock.accept()
print('client connected.')
while True:
     data = conn.recv(1024)
     if data.decode()=='exit':
         print('client disconnected')
         break
     msg = data.decode()
     conn.send(data)
     
     print('client: ',msg)
conn.close()