#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:56:33 2020

@author: user
"""

# TCP CLIENT 
"""
import socket
s= socket.socket()
# connect to the host
print("Socket Name: " ,socket.gethostname())
s.connect((socket.gethostname(),12346))
print("Connection created : ",s.recv(1024))
while True:
    data = s.recv(512)
    print(len(data))
    if (len(data) < 1):
        break
    print(data.decode(),end='')
s.close()
"""

# UDP CLIENT
"""
from socket import *
s = socket(AF_INET,SOCK_DGRAM)
#Create datagram socket
msg = "Hello World"
s.sendto(bytes(msg,"ascii"),("",10000))
data, addr = s.recvfrom(1000)
print(data)
"""

#Exercise 1
"""
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("www.wikipedia.org",80))
request=bytes('GET /index.html HTTP/1.0\n\n',"ascii")
s.send(request)
data = s.recv(10000)
print(data)
s.close()

"""

#Exercise 2
"""import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if (len(data) < 1):
			    break
	print(data.decode(),end='')
mysock.close()
"""
#Exercise
"""
import urllib
print(dir(urllib))
u=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
u_1 = urllib.request.urlopen("http://dr-chuck.com/page1.htm")
data = u.read()
print(data)
data1=u_1.read()
print(data1)
"""
#Exercise
"""
import urllib
fhand =urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
i=1
for line in fhand:
    text= line.decode()
    print(i," ",text)
    i=i+1
    
"""
#Exercise
"""
import urllib
fhand =urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts = dict()
for line in fhand:
    text= line.decode().split()
    for word in text:
        print(word,end=" ")
        counts[word]= counts.get(word,0)+1
    print()
print(counts)
"""
#Exercise

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
	print(line.decode().strip())
