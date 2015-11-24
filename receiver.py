# receiver.py

import numpy as np

from methods.settings import *

port_in = 1235
port_out = 1236


def get_frames(path, fps, width, height):
    print "Connecting with server. Starting to collect all frames."
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
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
    s.close()
    c.close()
    create_video(coll, path, fps, width, height)
    send_video()


def create_video(collection, path, fps, width, height):
    codec = cv2.VideoWriter_fourcc(*CODEC)
    out = cv2.VideoWriter('data/' + path, codec, fps, (width, height))
    print "Starting to change frames into video"
    for c in collection:
        frame = cv2.imdecode(c, 1)
        out.write(frame)
    print "Video has been created"
    out.release()


def send_video():
    print "Connecting with statistics"
    s = socket.socket()
    s.connect((HOST, port_out))
    s.send(PATH[i])
    s.close()
    print "Video path has been sent to statistics. Closing receiver."


if __name__ == '__main__':
    print "Starting receiver"
    for i in range(NUMBER_OF_VIDEOS):
        get_frames(PATH[i], FPS[i], WIDTH[i], HEIGHT[i])
