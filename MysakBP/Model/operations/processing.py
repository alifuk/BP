"""Filtry"""
import cv2
import numpy as np
import MysakBP.Model.Alvalidator as av


def smooth(img, params):

    '''Vyhlazení'''

    validator = av.Alvalidator(params)
    p_count_vertical = validator.int_validate(params[0], 'vertikální vyhlazení pixelů',4)
    p_count_horizontal = validator.int_validate(params[1], 'horizontální vyhlazení pixelů',4)
    if validator.evaluate() is False:
        return validator.filters_description


    kernel = np.ones((p_count_horizontal, p_count_vertical), np.float32) / (p_count_horizontal * p_count_vertical)
    return cv2.filter2D(img, -1, kernel)
