# client.py
import socket

import cv2
import numpy

host = socket.gethostname()
port_in = 1233
port_out = 1234

video_url = ""


def get_video_url():
    s = socket.socket()
    s.bind((host, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(1024)
        url = data
        c.send('Received video url.')
        break
    c.close()
    split_frames(url)


def send_message(message):
    s = socket.socket()
    s.connect((host, port_out))
    s.send(message)
    s.close()


def split_frames(video):
    cap = cv2.VideoCapture(video)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                result, imgencode = cv2.imencode('.jpg', frame, encode_param)
                data = numpy.array(imgencode)
                data_to_send = data.tobytes()
                send_message(data_to_send)
            else:
                break
        cap.release()
        send_message("stop")
    except socket.error:
        print 'Server is not responding. Shutting down.'


if __name__ == '__main__':
    get_video_url()
