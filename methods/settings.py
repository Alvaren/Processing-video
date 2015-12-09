# settings.py
import socket

import cv2

VIDEO_URL = "My_Movie_3s.avi"
# General processing
PATH = ['xvid.avi', 'mpeg.avi', 'mp42.avi', '40fps.avi', '50fps.avi', '20fps.avi', '10fps.avi', 'mog2.avi', 'knn.avi',
        '2048_1152.avi', '2048_1280.avi', '640_360.avi', '800_600.avi', 'colorspace.avi', 'threshold.avi',
        'translate_frame.avi', 'rotate_frame.avi', 'transformation.avi']
WIDTH = [1920, 1920, 1920, 1920, 1920, 1920, 1920, 1920, 1920, 2048, 2048, 640, 800, 1920, 1920, 1920, 1920, 1920]
HEIGHT = [1080, 1080, 1080, 1080, 1080, 1080, 1080, 1080, 1080, 1152, 1920, 360, 600, 1080, 1080, 1080, 1080, 1080]
FPS = [30.0, 30.0, 30.0, 40.0, 50.0, 20.0, 10.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0]
METHOD = ['None', 'None', 'None', 'fps', 'fps', 'fps', 'fps', 'mog2', 'knn', 'resolution', 'resolution', 'resolution',
          'resolution', 'colorspace', 'global threshold', 'translate frame', 'rotate frame', 'affine transformation']
# XVID, H264, MPEG, MP42
CODEC = ['XVID', 'MPEG', 'MP42', 'XVID', 'XVID', 'XVID', 'XVID', 'XVID', 'XVID', 'XVID', 'XVID', 'XVID', 'XVID', 'XVID',
         'XVID', 'XVID', 'XVID', 'XVID']

HOST = socket.gethostname()
ENCODE_PARAM = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
NUMBER_OF_VIDEOS = 18
