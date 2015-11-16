# client.py
import numpy

from methods.settings import *

port_in = 1233
port_out = 1234


def get_video_url():
    print "Connecting with video retriever"
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(1024)
        url = data
        print "Video url has been captured."
        c.send('Received video url.')
        break
    c.close()
    split_frames(url)


def send_message(message):
    s = socket.socket()
    s.connect((HOST, port_out))
    s.send(message)
    s.close()


def split_frames(video):
    print "Connecting with server. Starting to send frames."
    cap = cv2.VideoCapture(video)
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                encode_frame(frame)
            else:
                break
        print "All frames has been sent. Closing client."
        cap.release()
        send_message("stop")
    except socket.error:
        print 'Server is not responding. Shutting down.'


def encode_frame(frame):
    result, imgencode = cv2.imencode('.jpg', frame, ENCODE_PARAM)
    data = numpy.array(imgencode)
    data_to_send = data.tobytes()
    send_message(data_to_send)


if __name__ == '__main__':
    print "Starting client"
    get_video_url()
