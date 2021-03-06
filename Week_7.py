#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:20:07 2020

@author: user
"""

# TCP SERVER
"""
# creates a server
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
  conn.send(bytes('Thanks for connection',"ascii"))
  conn.send(bytes(addr[0],"ascii"))
  conn.close() # close client conncetion

  """
 
# UDP SERVER
"""from socket import *
s = socket(AF_INET,SOCK_DGRAM)
#Create datagram socket
#Bind to a specific port
s.bind(("",10000)) 
while True:
    data, addr = s.recvfrom(10000)
    print(data)
    resp = "Get off my lawn!"
    s.sendto(bytes(resp,"ascii"),addr)
    """
    
