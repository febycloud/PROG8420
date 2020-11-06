import socket

s= socket.socket()
# bind host and port
s.bind((socket.gethostname(),12346))

s.listen(5) # wait for client connection
while True:
	conn,addr = s.accept() # returns client_socket and address
	print("Got connection from ", addr)
	# use client socket for transmitting data.
	# Server socket is only used for accepting new connections
	conn.send('Thanks for connection'.encode())
	conn.send(bytes(addr[0],"ascii"))
	conn.close() # close client conncetion