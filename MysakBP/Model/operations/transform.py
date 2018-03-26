"""Transformace"""
import cv2
import MysakBP.Model.Alvalidator as av
import numpy as np

def rotate(img, params):
    """Rotace"""
    validator = av.Alvalidator(params)
    angle = validator.int_validate(params[0], 'Úhel', 0)
    if validator.evaluate() is False:
        return validator.filters_description



    rows, cols, channels = img.shape

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))

    return dst

def hough_lines(img, params):
    """Hough lines"""
    validator = av.Alvalidator(params)
    r = validator.int_validate(params[0], 'Rho', 50)
    t = validator.int_validate(params[1], 'Pi / Theta', 180)
    tresh = validator.int_validate(params[2], 'Threshold', 200)
    if validator.evaluate() is False:
        return validator.filters_description

    lines = cv2.HoughLines(img, r, np.pi / t, tresh)

    try:
        for rho, theta in lines[:,0,:]:
            print(theta)
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 10000 * (-b))
            y1 = int(y0 + 10000 * (a))
            x2 = int(x0 - 10000 * (-b))
            y2 = int(y0 - 10000 * (a))

            cv2.line(img, (x1, y1), (x2, y2), 255, 2)
    except:
        print('No lines')

    return img

def hough_circles(img, params):
    """Hough circles"""
    validator = av.Alvalidator(params)
    dp = validator.int_validate(params[0], 'dp', 1)
    min_dist = validator.int_validate(params[1], 'min_dist', 5)
    p1 = validator.int_validate(params[2], 'param1', 50)
    p2 = validator.int_validate(params[3], 'param2', 4)
    if validator.evaluate() is False:
        return validator.filters_description


    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp, min_dist,
                               param1=p1, param2=p2, minRadius=0, maxRadius=0)
    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(img, (i[0], i[1]), i[2], 100, 2)
            # draw the center of the circle
            cv2.circle(img, (i[0], i[1]), 2, 255, 3)
    except:
        print('No circles')
    return img


def crop(img, params):
    """Ořez"""
    validator = av.Alvalidator(params)
    xcrop = validator.float_validate(params[0], 'Ořez x', 1)
    ycrop = validator.float_validate(params[1], 'Ořez y', 1)
    if validator.evaluate() is False:
        return validator.filters_description

    return cv2.resize(img, None, fx=xcrop, fy=ycrop, interpolation=cv2.INTER_CUBIC)
