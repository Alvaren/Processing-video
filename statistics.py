# stastistics.py
import os
import time

import pygal

from methods.settings import *
from methods.video_details import *

port_in = 1236


def get_number_of_videos():
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(1024)
        c.send('Received the message.')
        break
    s.close()
    c.close()
    return data


def get_video_url(number_of_videos):
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
        if len(videos) == (int(float(number_of_videos)) + 1):
            break
    print "All video Urls has been received."
    c.close()
    return videos
    # print_data(videos)


def print_data(collection):
    for c in collection:
        metadata_for('data/video/' + c)
    print "All data has been shown. Stopping statistics."


def draw_graphs(videos):
    values = ['duration', 'bit_rate', 'frame_rate', 'width', 'height', 'size']
    values_with_unit = ['duration [sec]', 'bitRate[Mbit/s]', 'frameRate[fps]', 'width[pixels]',
                        'height[pixels]',
                        'size[Mb]']
    data = []
    for v in videos:
        tmp = []
        vid = metadata_for('data/video/' + v)
        for c in values:
            if c == 'duration':
                seconds = vid.get(c)
                tmp.append(seconds.total_seconds())
            elif c == 'bit_rate':
                bitrate = (vid.get(c) / float(1000000))
                tmp.append(bitrate)
            elif c == 'size':
                size = os.path.getsize('data/video/' + v) / 1000000
                tmp.append(size)
            else:
                tmp.append(vid.get(c))
        data.append(tmp)
    final_chart = pygal.Line(x_label_rotation=270)
    final_chart.title = 'Final Chart'
    final_chart.x_labels = videos
    for i in range(len(values)):
        line_chart = pygal.Line(x_label_rotation=270)
        line_chart.title = values_with_unit[i]
        line_chart.x_labels = videos
        asd = []
        for j in range(len(videos)):
            asd.append(data[j][i])
        line_chart.add(values_with_unit[i], asd)
        if values[i] != 'width' and values[i] != 'height':
            final_chart.add(values_with_unit[i], asd)
        line_chart.render_to_file('data/graphs/' + values[i] + '.svg')
    final_chart.render_to_file('data/graphs/final.svg')


def stop_launcher():
    try:
        s = socket.socket()
        s.connect((HOST, 1232))
        s.send("stop")
        s.close()
    except socket.error:
        print 'Failed to connect with launcher. Will try again in 10 seconds.'
        time.sleep(10)
        stop_launcher()


if __name__ == '__main__':
    print "Starting statistics"
    number = get_number_of_videos()
    video = get_video_url(number)
    draw_graphs(video)
    print 'All videos has been processed'
    stop_launcher()
