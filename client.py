# client.py
import socket

import cv2
import numpy

host = socket.gethostname()
port = 1234


def send_message(message):
    s = socket.socket()
    s.connect((host, port))
    s.send(message)
    s.close()


def split_frames():
    cap = cv2.VideoCapture("My_Movie.avi")
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
    split_frames()
