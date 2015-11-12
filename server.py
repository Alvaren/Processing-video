# server.py
import socket

import cv2
import numpy as np

s = socket.socket()
host = socket.gethostname()
port_in = 1234
port_out = 1235
s.bind((host, port_in))
s.listen(1)

fgbg = cv2.createBackgroundSubtractorMOG2()


def get_frames():
    print "Received data. Starting to decode video."
    coll = []
    while True:
        c, addr = s.accept()
        data = c.recv(300000)
        if data == "stop":
            c.send('Stopping the server.')
            break
        else:
            test = np.fromstring(data, dtype=np.uint8)
            coll.append(test)
            c.send('Received the message.')
    c.close()
    modify_frames(coll)


def modify_frames(collection):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    for c in collection:
        frame = cv2.imdecode(c, 1)
        fgmask = fgbg.apply(frame)
        frame = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = np.array(imgencode)
        data_to_send = data.tobytes()
        send_message(data_to_send)
    send_message("stop")


def send_message(message):
    s = socket.socket()
    s.connect((host, port_out))
    s.send(message)
    s.close()


if __name__ == '__main__':
    get_frames()
