# video_retriver.py
import socket

host_out = socket.gethostname()
port_out = 1233
video_url = "My_Movie.avi"


def send_message():
    s = socket.socket()
    s.connect((host_out, port_out))
    s.send(video_url)
    s.close()


if __name__ == '__main__':
    send_message()
