# stastistics.py
import socket
import pygal

from methods.video_details import *

host = socket.gethostname()
port_in = 1236
videos = []
categories = ['bitrate', 'fps']


def get_video_url():
    print "Connecting with receiver and client to receiver video urls."
    s = socket.socket()
    s.bind((host, port_in))
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


def test_graph(collection):
    line_chart = pygal.Line()
    line_chart.title = 'Test chart'
    for c in categories:
        line_chart.x_labels = map(str, range(0, 10))
        for v in collection:
            values = v
        line_chart.add(c, values)
        # line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
        # line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        # line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
        line_chart.render_to_file('graphs/' + c + '.svg')


def print_data(collection):
    for c in collection:
        metadata_for(c)
    print "All data has been shown. Stopping statistics."


if __name__ == '__main__':
    print "Starting statistics"
    test_graph()
