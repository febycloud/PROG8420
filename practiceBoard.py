import socket
s= socket.socket()
# connect to the host
print("Socket Name: " ,socket.gethostname())
s.connect((socket.gethostname(),12346))
print("Connection created : ",s.recv(512))
while True:
	data = s.recv(512)
	print('data long is ',len(data))
	print(data.decode(),end='\n')
	if (len(data) < 1):
		break
	
s.close()

