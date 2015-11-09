# server.py
import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(1)
original_collection = []
converted_collection = []


def get_data():
    while True:
        c, addr = s.accept()
        data = c.recv(4096)
        if data == "stop":
            c.send('Stopping the server.')
            break
        else:
            original_collection.append(data)
            converted_collection.append(do_stuff(data, 0))
            # print 'Got connection from', addr
            c.send('Received the message.')
    c.close()
    print_collection()


def do_stuff(data, index):
    return data + " 2"


def print_collection():
    for c in original_collection:
        print c

if __name__ == '__main__':
    get_data()
