# server.py
import time

from methods.video_processing import *

port_in = 1234
port_out = 1235


def get_number_of_videos():
    print 'Server: Connecting with video_retriever.'
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(1024)
        number = data
        c.send('Received the message.')
        break
    s.close()
    c.close()
    return number


def get_frames():
    print 'Server: Connecting with client. Starting to collect all frames.'
    frames = []
    s = socket.socket()
    s.bind((HOST, port_in))
    s.listen(1)
    while True:
        c, addr = s.accept()
        data = c.recv(350000)
        if data == "stop":
            c.send('Stopping the server.')
            break
        else:
            frame = np.fromstring(data, dtype=np.uint8)
            frames.append(frame)
            c.send('Received the message.')
    print 'Server: All frames has been received.'
    s.close()
    c.close()
    return frames


def modify_frames(collection, method, width, height):
    print 'Server: Starting to modify frames.'
    for c in collection:
        frame = cv2.imdecode(c, 1)
        encode_frame(frame, method, width, height)
    print 'Server: All frames has been modified.'


def encode_frame(frame, method, width, height):
    frame = video_process(frame, method, width, height)
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
        print 'Failed to connect with receiver. Will try again in 10 seconds.'
        time.sleep(10)
        send_message(message)


if __name__ == '__main__':
    print 'Server: Starting connections.'
    counter = int(float(get_number_of_videos()))
    frames = get_frames()
    modify_frames(frames, METHOD[0], WIDTH[0], HEIGHT[0])
    send_message("stop")
    for i in range(1, counter):
        modify_frames(frames, METHOD[i], WIDTH[i], HEIGHT[i])
        send_message("stop")
    print 'Server: All data has been sent. Closing connections.'
