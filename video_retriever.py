# video_retriever.py
import socket

host_out = socket.gethostname()
port_out = 1233
video_url = "My_Movie.avi"


def send_message():
    print "Connecting with client"
    s = socket.socket()
    s.connect((host_out, port_out))
    s.send(video_url)
    print "Video url has been send. Closing video retriever."
    s.close()


if __name__ == '__main__':
    print "Starting retrieving video."
    send_message()
