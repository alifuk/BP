import cv2
import numpy as np


def smooth(img, params):
    p_count_vertical = int(params[0])
    p_count_horizontal = int(params[1])
    kernel = np.ones((p_count_horizontal, p_count_vertical), np.float32) / (p_count_horizontal * p_count_vertical)
    return cv2.filter2D(img, -1, kernel)
