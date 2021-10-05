import socket
import datetime

flag = False
sock = socket.socket()
sock.bind(("", 1991))
sock.listen(2)
print(f"\33[93mServer launched on {datetime.datetime.now().strftime('%A, %d. %B %Y %I:%M%p')}\33[0m")

while True:
	msg=''
	conn, addr = sock.accept()
	name = conn.recv(1024).decode().capitalize()
	print(f'{name} \33[92mconnected!\33[0m')
	while True:
		data = conn.recv(1024)
		msg = data.decode().capitalize()
	
		if msg == "Exit":
			end_time = datetime.datetime.now().strftime('%A, %d. %B %Y %I:%M%p')
			conn.send(f"\33[91mConnection has ended on {end_time}\33[90m".encode())
			print(f"{name} \33[93mdisconnected\33[0m on {end_time}'\33[9m'")
			conn.close()
			break

		elif msg == "Off":
			print(f"\33[91mServer is turned off on {datetime.datetime.now().strftime('%A, %d. %B %Y %I:%M%p')} by user {name}\33[0m")
			conn.close()
			sock.close()
			flag = True
			break

		else:
			print(f"\33[7m{name.capitalize()}\33[0m: {msg.capitalize()}")
			conn.send(f'\33[93mYour message sent on {datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")}\33[0m'.encode())

	if flag:
		break

sock.close()