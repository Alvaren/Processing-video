# video_retriver.py
import socket

host = socket.gethostname()
port = 1234


def test():
    import urllib
    test = urllib.FancyURLopener()
    test.retrieve("https://drive.google.com/open?id=0B4bL21Dzu8MwdkZMX0xNZGFyZVk", "testout.mp4")
    print "done"


if __name__ == '__main__':
    test()