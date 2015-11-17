# server.py
import time
from methods.video_processing import *

port_in = 1234
port_out = 1235
frames = []


def get_frames():
    print "Connecting with client. Starting to collect all frames."
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(300000)
        if data == "stop":
            c.send('Stopping the server.')
            break
        else:
            frame = np.fromstring(data, dtype=np.uint8)
            frames.append(frame)
            c.send('Received the message.')
    print "All frames has been received."
    s.close()
    c.close()
    modify_frames(frames)


def modify_frames(collection):
    print "Starting to modify frames."
    for c in collection:
        frame = cv2.imdecode(c, 1)
        encode_frame(frame)
    send_message("stop")
    print "All frames has been modified. Stopping server."


def encode_frame(frame):
    frame = video_process(frame)
    result, imgencode = cv2.imencode('.jpg', frame, ENCODE_PARAM)
    data = np.array(imgencode)
    data_to_send = data.tobytes()
    send_message(data_to_send)


def send_message(message):
    try:
        s = socket.socket()
        s.connect((HOST, port_out))
        s.send(message)
        s.close()
    except socket.error:
        print 'Failed to connect with receiver. Will try again in 5 seconds.'
        time.sleep(3)
        send_message(message)


if __name__ == '__main__':
    print "Starting server"
    get_frames()
    modify_frames(frames)
