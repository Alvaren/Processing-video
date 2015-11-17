# settings.py
import socket

import cv2

PATH = 'data/test.avi'
WIDTH = 1920
HEIGHT = 1080
FPS = 30.0
METHOD = 'mog2'
CODEC = 'XVID'
HOST = socket.gethostname()
ENCODE_PARAM = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
NUMBER_OF_VIDEOS = 2
