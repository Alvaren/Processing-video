# client.py
import time

import numpy

from methods.settings import *

port_in = 1233
port_out = 1234


def get_video_url():
    print 'Client: Connecting with video_retriever.'
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(1024)
        url = data
        print 'Client: Video path has been captured.'
        c.send('Received video url.')
        break
    c.close()
    return url


def send_message(message):
    try:
        s = socket.socket()
        s.connect((HOST, port_out))
        s.send(message)
        s.close()
    except socket.error:
        print 'Client: Failed to connect with server. Will try again in 10 seconds.'
        time.sleep(10)
        send_message(message)


def split_frames(video):
    print 'Client: Connecting with server. Starting to send frames.'
    cap = cv2.VideoCapture('data/video/' + video)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            encode_frame(frame)
        else:
            break
    cap.release()


def encode_frame(frame):
    result, imgencode = cv2.imencode('.jpg', frame, ENCODE_PARAM)
    data = numpy.array(imgencode)
    data_to_send = data.tobytes()
    send_message(data_to_send)


if __name__ == '__main__':
    print 'Client: Starting connections.'
    url = get_video_url()
    split_frames(url)
    send_message("stop")
    print 'Client: All data has been sent. Closing connections.'
