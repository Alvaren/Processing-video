# receiver.py
import socket

import cv2
import numpy as np

s = socket.socket()
host = socket.gethostname()
port_in = 1235
port_out = 1236
s.bind((host, port_in))
s.listen(1)

codec = cv2.VideoWriter_fourcc(*'XVID')
video_path = 'data/test.avi'
out = cv2.VideoWriter(video_path, codec, 30.0, (1920, 1080))


def get_frames():
    print "Connecting with server. Starting to collect all frames."
    coll = []
    while True:
        c, addr = s.accept()
        data = c.recv(350000)
        if data == "stop":
            c.send('Stopping the server.')
            break
        else:
            test = np.fromstring(data, dtype=np.uint8)
            coll.append(test)
            c.send('Received the message.')
    print "All frames has been received"
    c.close()
    create_video(coll)
    send_video()


def create_video(collection):
    print "Starting to change frames into video"
    for c in collection:
        frame = cv2.imdecode(c, 1)
        out.write(frame)
    print "Video has been created"
    out.release()


def send_video():
    print "Connecting with statistics"
    s = socket.socket()
    s.connect((host, port_out))
    s.send(video_path)
    s.close()
    print "Video path has been sent to statistics. Closing receiver."


if __name__ == '__main__':
    print "Starting receiver"
    get_frames()
