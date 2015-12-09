# stastistics.py
import os

import pygal

from methods.settings import *
from methods.video_details import *

port_in = 1236


def get_video_url():
    print "Connecting with receiver and client to receiver video urls."
    videos = []
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(1024)
        videos.append(data)
        print data
        c.send('Received video url.')
        if len(videos) == (NUMBER_OF_VIDEOS + 1):
            break
    print "All video Urls has been received."
    c.close()
    return videos
    # print_data(videos)


def print_data(collection):
    for c in collection:
        metadata_for('data/' + c)
    print "All data has been shown. Stopping statistics."


def draw_graphs(videos):
    values = ['duration', 'bit_rate', 'frame_rate', 'width', 'height', 'size']
    values_with_unit = ['duration [sec]', 'bitRate[Mbit/s]', 'frameRate[fps]', 'width[pixels]',
                        'height[pixels]',
                        'size[Mb]']
    data = []
    for v in videos:
        tmp = []
        vid = metadata_for('data/' + v)
        for c in values:
            if c == 'duration':
                seconds = vid.get(c)
                tmp.append(seconds.total_seconds())
            elif c == 'bit_rate':
                bitrate = (vid.get(c) / float(1000000))
                tmp.append(bitrate)
            elif c == 'size':
                size = os.path.getsize('data/' + v) / 1000000
                tmp.append(size)
            else:
                tmp.append(vid.get(c))
        data.append(tmp)
    final_chart = pygal.Line(x_label_rotation=270)
    final_chart.title = 'Final Chart - 30s video'
    final_chart.x_labels = videos
    for i in range(len(values)):
        line_chart = pygal.Line(x_label_rotation=270)
        line_chart.title = values_with_unit[i] + ' - 30s video'
        line_chart.x_labels = videos
        asd = []
        for j in range(len(videos)):
            asd.append(data[j][i])
        line_chart.add(values_with_unit[i], asd)
        if values[i] != 'width' and values[i] != 'height':
            final_chart.add(values_with_unit[i], asd)
        line_chart.render_to_file('graphs/' + values[i] + '.svg')
    final_chart.render_to_file('graphs/final.svg')


if __name__ == '__main__':
    print "Starting statistics"
    video = get_video_url()
    draw_graphs(video)
    print ''
    print 'All videos has been processed'
    path = os.path.dirname(os.path.realpath('__file__')) + '/graphs/final.svg'
    os.startfile(path)
