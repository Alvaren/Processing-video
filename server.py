# server.py
import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(1)
collection = []


def get_data():
    while True:
        # get all data
        c, addr = s.accept()
        data = c.recv(4096)
        if data == "stop":
            c.send('Stopping the server.')
            break
        else:
            collection.append(data)
            print 'Got connection from', addr
            c.send('Received the message.')
    c.close()
    print_collection()


def print_collection():
    for c in collection:
        print c

if __name__ == '__main__':
    get_data()
