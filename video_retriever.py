# video_retriever.py
import time

from methods.settings import *

port_out = 1233
port_statistics = 1236


def send_message(host_name, port):
    print "Connecting with " + host_name
    try:
        s = socket.socket()
        s.connect((HOST, port))
        s.send(VIDEO_URL)
        print "Video url has been send. Closing video retriever."
        s.close()
    except socket.error:
        print 'Failed to connect with ' + host_name + '. Will try again in 10 seconds.'
        time.sleep(10)
        send_message(host_name, port)


if __name__ == '__main__':
    print "Starting retrieving video."
    send_message('client', port_out)
    send_message('statistics', port_statistics)
