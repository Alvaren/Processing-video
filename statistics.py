# stastistics.py

from methods.settings import *
from methods.video_details import *

port_in = 1236
videos = []
categories = ['duration', 'bit_rate', 'frame_rate', 'width', 'height']


def get_video_url():
    print "Connecting with receiver and client to receiver video urls."
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(1024)
        videos.append(data)
        c.send('Received video url.')
        break
    print "All video Urls has been received."
    c.close()
    print_data(videos)


def print_data(collection):
    for c in collection:
        metadata_for(c)
    print "All data has been shown. Stopping statistics."


if __name__ == '__main__':
    print "Starting statistics"
    get_video_url()
