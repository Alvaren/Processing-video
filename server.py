# server.py
import socket
from methods.video_processing import *
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
    print "Connecting with client. Starting to collect all frames."
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
    print "All frames has been received."
    c.close()
    modify_frames(coll)


def modify_frames(collection):
    print "Starting to modify frames."
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    for c in collection:
        frame = cv2.imdecode(c, 1)
        frame = remove_background(frame)
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = np.array(imgencode)
        data_to_send = data.tobytes()
        send_message(data_to_send)
    send_message("stop")
    print "All frames has been modified. Stopping server."


def send_message(message):
    s = socket.socket()
    s.connect((host, port_out))
    s.send(message)
    s.close()


if __name__ == '__main__':
    print "Starting server"
    get_frames()
