# video_processing.py
import numpy as np

from methods.settings import *

fgbg_mog2 = cv2.createBackgroundSubtractorMOG2()
fgbg_knn = cv2.createBackgroundSubtractorKNN()


def background_subtractor_mog2(frame):
    try:
        fgmask = fgbg_mog2.apply(frame)
        frame = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
        return frame
    except:
        return frame


def background_subtractor_knn(frame):
    try:
        fgmask = fgbg_knn.apply(frame)
        frame = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
        return frame
    except:
        return frame


def frame_resize(frame, width, height):
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_CUBIC)
    return frame


def remove_background(frame):
    height, width = frame.shape[:2]
    mask = np.zeros(frame.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (10, 10, width - 30, height - 30)
    cv2.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img1 = frame * mask[:, :, np.newaxis]
    background = frame - img1
    background[np.where((background > [0, 0, 0]).all(axis=2))] = [255, 255, 255]
    frame = background + img1
    return frame


def change_colorspace(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    return res


def global_threshold(frame):
    ret1, th1 = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)
    return th1


def translate_frame(frame, width, height, direction_x, direction_y):
    M = np.float32([[1, 0, direction_x], [0, 1, direction_y]])
    dst = cv2.warpAffine(frame, M, (width, height))
    return frame_resize(dst, width, height)


def rotate_frame(frame, width, height, angle):
    M = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    dst = cv2.warpAffine(frame, M, (width, height))
    return frame_resize(dst, width, height)


def affine_transformation(frame, width, height):
    rows, cols, ch = frame.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(frame, M, (cols, rows))
    return frame_resize(dst, width, height)


def video_process(frame, method, width, height):
    if method == 'None':
        return frame
    elif method == 'fps':
        return frame
    elif method == 'knn':
        return background_subtractor_knn(frame)
    elif method == 'mog2':
        return background_subtractor_mog2(frame)
    elif method == 'own':
        return remove_background(frame)
    elif method == 'colorspace':
        return change_colorspace(frame)
    elif method == 'global threshold':
        return global_threshold(frame)
    elif method == 'translate frame':
        return translate_frame(frame, width, height, 100, 50)
    elif method == 'rotate frame':
        return rotate_frame(frame, width, height, 90)
    elif method == 'affine transformation':
        return affine_transformation(frame, width, height)
    else:
        return frame_resize(frame, width, height)
