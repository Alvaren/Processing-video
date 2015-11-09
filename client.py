# client.py
import socket

host = socket.gethostname()
port = 1234


def send_message(message):
    s = socket.socket()
    s.connect((host, port))
    s.send(message)
    print s.recv(4096)
    s.close()


def split_frames():
    try:
        # while True:
        for x in range(0, 4):
            send_message("hello world")
        # Send message to stop the server
        send_message("stop")
    except socket.error:
        print 'Server is not responding. Shutting down.'

if __name__ == '__main__':
    split_frames()
