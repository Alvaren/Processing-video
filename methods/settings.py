# settings.py
import socket

import cv2

PATH = ['data/no_change.avi', 'data/40fps.avi', 'data/50fps.avi', 'data/20fps.avi', 'data/10fps.avi', 'data/mog2.avi',
        'data/knn.avi', 'data/2048_1152_resolution.avi', 'data/2048_1280_resolution.avi', 'data/640_360_resolution.avi',
        'data/800_600_resolution.avi']
WIDTH = [1920, 1920, 1920, 1920, 1920, 1920, 1920, 2048, 2048, 640, 800]
HEIGHT = [1080, 1080, 1080, 1080, 1080, 1080, 1080, 1152, 1280, 360, 600]
FPS = [30.0, 40.0, 50.0, 20.0, 10.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0]
METHOD = ['None', 'fps', 'fps', 'fps', 'fps', 'mog2', 'knn', 'resolution', 'resolution', 'resolution', 'resolution']
CODEC = 'XVID'
HOST = socket.gethostname()
ENCODE_PARAM = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
NUMBER_OF_VIDEOS = 11
