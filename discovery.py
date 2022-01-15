from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('0.0.0.0',9000))
while 1:
	try:
		data, addr = server.recvfrom(1024)
		if data == b'raspberrypi':
			server.sendto(b'raspberrypi', addr)
			break
		else:
			print('Wrong client')
	except:
		break

