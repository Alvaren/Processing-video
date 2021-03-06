# video_retriever.py
import time

from methods.settings import *

port_in = 1232
port_out = 1233
port_statistics = 1236


def get_video_url():
    print 'VideoRetriever: Connecting with launcher.'
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
    s.close()
    c.close()
    return values


def send_message(host_name, port, path):
    print 'VideoRetriever: Connecting with ' + host_name + '.'
    try:
        s = socket.socket()
        s.connect((HOST, port))
        s.send(path)
        s.close()
    except socket.error:
        print 'VideoRetriever: Failed to connect with ' + host_name + '. Will try again in 10 seconds.'
        time.sleep(10)
        send_message(host_name, port, path)


if __name__ == '__main__':
    print "VideoRetriever: Starting connections."

    data = get_video_url()
    video_path = data[0]
    number_of_videos = data[1]

    send_message('server', 1234, number_of_videos)
    send_message('receiver', 1235, number_of_videos)
    send_message('statistics', 1236, number_of_videos)

    send_message('client', port_out, video_path)
    send_message('statistics', port_statistics, video_path)
    print 'VideoRetriever: All data has been sent. Closing connections.'
