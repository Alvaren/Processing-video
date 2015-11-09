# server.py
import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print c.recv(1024)
    print 'Got connection from', addr
    c.send('Thank you for your connecting')
    c.close()
