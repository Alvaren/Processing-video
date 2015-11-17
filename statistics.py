# stastistics.py
import os

import pygal

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
        if len(videos) == (NUMBER_OF_VIDEOS + 1):
            break
    print "All video Urls has been received."
    c.close()
    print_data(videos)


def print_data(collection):
    for c in collection:
        metadata_for(c)
    print "All data has been shown. Stopping statistics."


def draw_graphs():
    values = ['duration', 'bit_rate', 'frame_rate', 'width', 'height', 'size']
    data = []
    for v in PATH:
        tmp = []
        vid = metadata_for(v)
        for c in values:
            if c == 'duration':
                seconds = vid.get(c)
                tmp.append(seconds.total_seconds())
            elif c == 'bit_rate':
                bitrate = (vid.get(c) / float(1000000))
                tmp.append(bitrate)
            elif c == 'size':
                size = os.path.getsize(v) / 1000000
                tmp.append(size)
            else:
                tmp.append(vid.get(c))
        data.append(tmp)
    final_chart = pygal.Line()
    final_chart.title = 'Final Chart'
    final_chart.x_labels = PATH
    for i in range(len(values)):
        line_chart = pygal.Line()
        line_chart.title = values[i]
        line_chart.x_labels = PATH
        asd = []
        for j in range(len(PATH)):
            asd.append(data[j][i])
        line_chart.add(values[i], asd)
        if values[i] != 'width' and values[i] != 'height':
            final_chart.add(values[i], asd)
        line_chart.render_to_file('graphs/'+ values[i] + '.svg')
    final_chart.render_to_file('graphs/final.svg')


if __name__ == '__main__':
    print "Starting statistics"
    get_video_url()
    draw_graphs()
