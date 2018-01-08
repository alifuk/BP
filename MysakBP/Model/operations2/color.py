"""Barvy"""
import cv2
import MysakBP.Model.Alvalidator as av


def bw(img, params):
    """Konverze do černobílé"""
    for y in range(0, img.__len__()):
        for x in range(0, img[0].__len__()):
            img[y][x][1] = 0

    return img


def fcr(img, params):
    """Filtrace barevného rozsahu"""
    for y in range(0, img.__len__()):
        for x in range(0, img[0].__len__()):
            if img[y][x][0] < 100 or img[y][x][0] > 150:
                img[y][x][1] = 0

    return img


def convert(img, params):
    """Změna barevného prostoru"""
    validator = av.Alvalidator()
    colorspace_from = validator.range_validate(params[0], 'Původní barevný prostor', ['GRAY', 'BGR', 'HSV'])
    colorspace_to = validator.range_validate(params[1], 'Cílový barevný prostor', ['GRAY', 'BGR', 'HSV'])
    if validator.evaluate() is False:
        return validator.filters_description

    try:
        conversion_name = getattr(cv2, 'COLOR_' + colorspace_from + '2' + colorspace_to)
        img = cv2.cvtColor(img, conversion_name)
        print('heres')
    except:
        print('wrong conversion')
        pass

    return img
