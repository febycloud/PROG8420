#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from datetime import datetime

def accept_incoming_connections():
	"""Sets up handling for incoming clients."""
	while True:
		client, client_address = SERVER.accept()
		print("%s:%s has connected." % client_address)
		client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
		addresses[client] = client_address
		Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
	"""Handles a single client connection."""

	name = client.recv(BUFSIZ).decode("utf8")
	welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
	client.send(bytes(welcome, "utf8"))
	#msg = "%s has joined the chat!" % name
	clients[client] = name	
	msg= name+" just connected, now "+str(len(clients))+" member in room"
	print(clients)
	broadcast(bytes(msg, "utf8"))

	while True:
		msg = client.recv(BUFSIZ)
		if msg != bytes("{quit}", "utf8"):
			timenw=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
			print(clients)
			broadcast(msg, timenw+" "+name+": ")
		else:
			client.send(bytes("{quit}", "utf8"))
			client.close()
			del clients[client]
			print(clients)
			broadcast(bytes(name+" has left chat, now "+str(len(clients))+" member in room", "utf8"))
			break


def broadcast(msg, prefix=""):  # prefix is for name identification.
	"""Broadcasts a message to all the clients."""

	for sock in clients:
		sock.send(bytes(prefix, "utf8")+msg)

		
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
	SERVER.listen(5)
	print("Waiting for connection...")
	ACCEPT_THREAD = Thread(target=accept_incoming_connections)
	ACCEPT_THREAD.start()
	ACCEPT_THREAD.join()
	SERVER.close()
	