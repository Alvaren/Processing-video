# receiver.py
import socket

import cv2
import numpy as np

s = socket.socket()
host = socket.gethostname()
port_in = 1235
s.bind((host, port_in))
s.listen(1)

codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test.avi', codec, 29.0, (1920, 1080))


def get_frames():
    print "Received data. Starting to decode video."
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
    c.close()
    create_video(coll)


def create_video(collection):
    for c in collection:
        frame = cv2.imdecode(c, 1)
        out.write(frame)
    out.release()


if __name__ == '__main__':
    get_frames()
