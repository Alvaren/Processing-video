# video_retriever.py
import time

from methods.settings import *

port_in = 1232
port_out = 1233
port_statistics = 1236


def get_video_url():
    print "Connecting with video retriever"
    values = []
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(1024)
        if data == "stop":
            c.send('Stopping the server.')
            break
        else:
            values.append(data)
            c.send('Received data.')
    c.close()
    return values


def send_message(host_name, port, path):
    print "Connecting with " + host_name
    try:
        s = socket.socket()
        s.connect((HOST, port))
        s.send(path)
        print "Video url has been send. Closing video retriever."
        s.close()
    except socket.error:
        print 'Failed to connect with ' + host_name + '. Will try again in 10 seconds.'
        time.sleep(10)
        send_message(host_name, port, path)


if __name__ == '__main__':
    print "Connecting with launcher."
    data = get_video_url()
    video_path = data[0]
    NUMBER_OF_VIDEOS = data[1]
    print NUMBER_OF_VIDEOS
    print "Sending video to client."
    send_message('client', port_out, video_path)
    print "Sending video to statistics."
    send_message('statistics', port_statistics, video_path)
