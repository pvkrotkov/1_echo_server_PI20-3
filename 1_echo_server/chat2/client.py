import socket, threading, time

key = 8194

shutdown = False
join = False

def receving (name, sock):
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				#print(data.decode("utf-8"))

				# Begin
				decrypt = ""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)
				# End

				time.sleep(0.2)
		except:
			pass

host = "127.0.0.1"
port = 0

server = ("127.0.0.1",9090)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

alias = input("Name: ")

#threads so others can see the message while typing
rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()

while shutdown == False:
	#new user
	if join == False:
		s.sendto(("["+alias + "] => join chat ").encode("utf-8"),server)
		join = True
	#user was already in chat
	else:
		try:
			message = input()

			# crypting user's message
			crypt = ""
			for i in message:
				crypt += chr(ord(i)^key)
			message = crypt
			
			#check that message is not empty
			if message != "":
				s.sendto(("["+alias + "] : "+message).encode("utf-8"),server)
			
			#sleeptime for server to not crush
			time.sleep(0.2)
		except:
			#ctrl c option leaving chat
			s.sendto(("["+alias + "] <= left chat ").encode("utf-8"),server)
			shutdown = True

rT.join()
s.close()