import cv2


def rotate(img, params):
    angle = int(params[0])
    rows, cols, channels = img.shape

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))

    return dst


def crop(img, params):
    xcrop = float(params[0])
    ycrop = float(params[1])
    return cv2.resize(img, None, fx=xcrop, fy=ycrop, interpolation=cv2.INTER_CUBIC)
