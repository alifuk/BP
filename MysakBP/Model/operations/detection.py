"""Detekce"""
import cv2
import numpy as np
import MysakBP.Model.Alvalidator as av


def corner(img, params):
    """Detekce hran"""
    validator = av.Alvalidator(params)
    corner_count = validator.string_validate(params[0], 'Maximální počet hran k nalezení')
    threshold = validator.string_validate(params[1], 'Práh')
    minimum_distance = validator.string_validate(params[2], 'Minimální vzdálenost hran')
    if validator.evaluate() is False:
        return validator.filters_description


    rgb = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

    corner_count = int(corner_count)
    threshold = float(threshold)
    minimum_distance = int(minimum_distance)
    corners = cv2.goodFeaturesToTrack(gray, corner_count, threshold, minimum_distance)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 15, 255, -1)
    return img

def component(img, params):
    """Pozice komponent"""
    validator = av.Alvalidator(params)
    if validator.evaluate() is False:
        return validator.filters_description

    pole = []
    for y in range(0, len(img[0])):
        for x in range(0, len(img)):
            if img[x][y] != 0:
                pole.append([x, y])

    ciste_pole = []

    for i in range(0, len(pole)):
        pridat = True

        for j in range(0, len(ciste_pole)):

            if (pole[i][0] - ciste_pole[j][0]) ** 2 + (pole[i][1] - ciste_pole[j][1]) ** 2 < 1000:
                pridat = False

        if pridat:
            ciste_pole.append(pole[i])

    return ciste_pole
