import cv2
import numpy as np

fgbg_mog2 = cv2.createBackgroundSubtractorMOG2()
fgbg_knn = cv2.createBackgroundSubtractorKNN()


def background_subtractor_mog2(frame):
    fgmask = fgbg_mog2.apply(frame)
    frame = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
    return frame


def background_subtractor_knn(frame):
    fgmask = fgbg_knn.apply(frame)
    frame = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
    return frame


def remove_background(frame):
    height, width = frame.shape[:2]
    # Create a mask holder
    mask = np.zeros(frame.shape[:2], np.uint8)
    # Grab Cut the object
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    # Hard Coding the Rect The object must lie within this rect.
    rect = (10, 10, width - 30, height - 30)
    cv2.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img1 = frame * mask[:, :, np.newaxis]
    # Get the background
    background = frame - img1
    # Change all pixels in the background that are not black to white
    background[np.where((background > [0, 0, 0]).all(axis=2))] = [255, 255, 255]
    # Add the background and the image
    frame = background + img1
    return frame


def video_process(frame):
    return background_subtractor_mog2(frame)
