import cv2
import numpy as np
import MysakBP.Model.Alvalidator as av


def corner(img, params):

    validator = av.Alvalidator(params)
    params[0] = validator.string_validate(params[0], 'Maximální počet hran k nalezení')
    params[1] = validator.string_validate(params[2], 'Treshold')
    params[2] = validator.string_validate(params[1], 'Minimální vzdálenost hran')
    if validator.evaluate() is False:
        return validator.filters_description


    rgb = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

    corner_count = int(params[0])
    threshold = float(params[1])
    minimum_distance = int(params[2])
    corners = cv2.goodFeaturesToTrack(gray, corner_count, threshold, minimum_distance)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 15, 255, -1)
    return img

