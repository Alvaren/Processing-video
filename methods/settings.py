# settings.py
import socket

import cv2

PATH = ['no_change.avi', '40fps.avi', '50fps.avi', '20fps.avi', '10fps.avi', 'mog2.avi',
        'knn.avi', '2048_1152_resolution.avi', '2048_1280_resolution.avi', '640_360_resolution.avi',
        '800_600_resolution.avi', 'own_implementation.avi']
WIDTH = [1920, 1920, 1920, 1920, 1920, 1920, 1920, 2048, 2048, 640, 800, 1920]
HEIGHT = [1080, 1080, 1080, 1080, 1080, 1080, 1080, 1152, 1280, 360, 600, 1080]
FPS = [30.0, 40.0, 50.0, 20.0, 10.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0]
METHOD = ['None', 'fps', 'fps', 'fps', 'fps', 'mog2', 'knn', 'resolution', 'resolution', 'resolution', 'resolution',
          'own']
# XVID, H264, MPEG, MP42
CODEC = 'XVID'
HOST = socket.gethostname()
ENCODE_PARAM = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
NUMBER_OF_VIDEOS = 11
