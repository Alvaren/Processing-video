# client.py
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
s.send("hello world")
print s.recv(1024)
