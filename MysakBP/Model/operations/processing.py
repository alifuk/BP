"""Zpracování obrazu"""
import cv2
import numpy as np
import MysakBP.Model.Alvalidator as av


def tresholding(img, params):

    '''Prahování'''

    validator = av.Alvalidator(params)
    treshold = validator.int_validate(params[0], 'hodnota spodního prahu',155)
    treshold_top = validator.int_validate(params[1], 'hodnota horního prahu',255)
    if validator.evaluate() is False:
        return validator.filters_description

    ret, thresh1 = cv2.threshold(img, treshold, 255, cv2.THRESH_BINARY)
    thresh1 = 255 - thresh1
    ret, thresh2 = cv2.threshold(img, treshold_top, 255, cv2.THRESH_BINARY)
    t = thresh1 + thresh2


    return 255 - t

def coloring(img, params):

    '''Barvení oblastí'''

    validator = av.Alvalidator(params)
    if validator.evaluate() is False:
        return validator.filters_description

    # Marker labelling
    ret, markers = cv2.connectedComponents(img)
    print('marks:')
    print(markers.shape)
    print(ret)
    markers = markers * 25
    markers[markers == 0] = 255
    return markers


def morphology(img, params):

    '''Bin. morfologické operace'''

    validator = av.Alvalidator(params)
    type = validator.range_validate(params[1], 'Typ morfologie', ['Eroze', 'Diletace', 'Otevření', 'Uzavření'],'Eroze')
    kernel_size = validator.range_validate(params[2], 'Velikost jádra', ['3', '5', '7'],'3')
    iteration_count = validator.int_validate(params[0], 'Počet iterací', 1)

    if validator.evaluate() is False:
        return validator.filters_description
    kernel_size = int(kernel_size)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)


    if type == 'Eroze':
        img = cv2.erode(img, kernel, iterations=iteration_count)
    if type == 'Diletace':
        img = cv2.dilate(img, kernel, iterations=iteration_count)
    if type == 'Otevření':
        for n in range(0, iteration_count):
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    if type == 'Uzavření':
        for n in range(0, iteration_count):
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    return img
