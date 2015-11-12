# server.py
import socket

import cv2
import numpy as np

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(1)
fgbg = cv2.createBackgroundSubtractorMOG2()

codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test.avi', codec, 29.0, (1920, 1080))


def get_data():
    while True:
        c, addr = s.accept()
        data = c.recv(300000)
        if data == "stop":
            c.send('Stopping the server.')
            break
        else:
            test = np.fromstring(data, dtype=np.uint8)
            frame = cv2.imdecode(test, 1)
            fgmask = fgbg.apply(frame)
            frame = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
            out.write(frame)
            c.send('Received the message.')
    c.close()
    out.release()


if __name__ == '__main__':
    get_data()
