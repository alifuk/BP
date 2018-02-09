"""Zpracování obrazu"""
import cv2
import numpy as np
import MysakBP.Model.Alvalidator as av


def tresholding(img, params):

    '''Prahování'''

    validator = av.Alvalidator(params)
    treshold = validator.int_validate(params[0], 'hodnota prahu',155)
    if validator.evaluate() is False:
        return validator.filters_description

    ret, thresh1 = cv2.threshold(img, treshold, 255, cv2.THRESH_BINARY)
    return thresh1

def morphology(img, params):

    '''Morfologické transformace'''

    validator = av.Alvalidator(params)
    type = validator.range_validate(params[0], 'Typ morfologie', ['Eroze', 'Diletace'],'Eroze')
    if validator.evaluate() is False:
        return validator.filters_description

    if type == 'Eroze':
        kernel = np.ones((7, 7), np.uint8)
        erosion = cv2.erode(img, kernel, iterations=1)
    if type == 'Diletace':
        kernel = np.ones((7, 7), np.uint8)
        erosion = cv2.dilate(img, kernel, iterations=1)
    return erosion
