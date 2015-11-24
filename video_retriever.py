# video_retriever.py
from methods.settings import *

port_out = 1233
port_statistics = 1236
video_url = "My_Movie.avi"


def send_message(port):
    print "Connecting with client"
    try:
        s = socket.socket()
        s.connect((HOST, port))
        s.send(video_url)
        print "Video url has been send. Closing video retriever."
        s.close()
    except socket.error:
        print 'Client is not responding. Shutting down.'


if __name__ == '__main__':
    print "Starting retrieving video."
    send_message(port_out)
    send_message(port_statistics)
