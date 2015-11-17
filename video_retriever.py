# video_retriever.py
from methods.settings import *

port_out = 1233
video_url = "data/My_Movie.avi"


def send_message():
    print "Connecting with client"
    try:
        s = socket.socket()
        s.connect((HOST, port_out))
        s.send(video_url)
        print "Video url has been send. Closing video retriever."
        s.close()
    except socket.error:
        print 'Client is not responding. Shutting down.'


if __name__ == '__main__':
    print "Starting retrieving video."
    send_message()
