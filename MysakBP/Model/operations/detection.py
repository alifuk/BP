import cv2
import numpy as np


def corner(img, params):

    rgb = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

    corner_count = int(params[0])
    treshold = float(params[1])
    minimum_distance = int(params[2])
    corners = cv2.goodFeaturesToTrack(gray, corner_count, treshold, minimum_distance)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 15, 255, -1)
    return img

