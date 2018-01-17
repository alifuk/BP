"""Transformace"""
import cv2
import MysakBP.Model.Alvalidator as av

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


def crop(img, params):
    """Ořez"""
    validator = av.Alvalidator(params)
    xcrop = validator.float_validate(params[0], 'Ořez x', 1)
    ycrop = validator.float_validate(params[1], 'Ořez y', 1)
    if validator.evaluate() is False:
        return validator.filters_description

    return cv2.resize(img, None, fx=xcrop, fy=ycrop, interpolation=cv2.INTER_CUBIC)
