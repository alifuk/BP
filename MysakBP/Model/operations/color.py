"""Barvy"""
import cv2
import MysakBP.Model.Alvalidator as av


def convertColor(img, params):
    """Změna barevného prostoru"""
    validator = av.Alvalidator(params)
    colorspace_from = validator.range_validate(params[0], 'Původní barevný prostor', ['GRAY', 'BGR', 'HSV', 'YCR_CB'],
                                               1)
    colorspace_to = validator.range_validate(params[1], 'Cílový barevný prostor', ['GRAY', 'BGR', 'HSV', 'YCR_CB'], 2)
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


def getComponent(img, params):
    """Získat komponentu"""
    validator = av.Alvalidator(params)
    array_of_color_components = [
        'GRAY',
        'BGR(B)',
        'BGR(G)',
        'BGR(R)',
        'HSV(H)',
        'HSV(S)',
        'HSV(V)',
        'YCR_CB(Y)',
        'YCR_CB(CR)',
        'YCR_CB(CB)'
    ]
    component_to_get = validator.range_validate(params[0], 'Získat komponentu', array_of_color_components, 0)
    if validator.evaluate() is False:
        return validator.filters_description

    try:
        if 'GRAY' in component_to_get:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif 'BGR' in component_to_get:
            if '(B)' in component_to_get:
                img = img[:, :, 0]
            elif '(G)' in component_to_get:
                img = img[:, :, 1]
            elif '(R)' in component_to_get:
                img = img[:, :, 2]
        elif 'HSV' in component_to_get:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            if '(H)' in component_to_get:
                img = img[:, :, 0]
            elif '(S)' in component_to_get:
                img = img[:, :, 1]
            elif '(V)' in component_to_get:
                img = img[:, :, 2]
        elif 'YCR_CB' in component_to_get:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
            if '(Y)' in component_to_get:
                img = img[:, :, 0]
            elif '(CR)' in component_to_get:
                img = img[:, :, 1]
            elif '(CB)' in component_to_get:
                img = img[:, :, 2]
    except:
        print('wrong conversion')
        pass

    return img


def fcr(img, params):
    """Filtrace barevného rozsahu"""
    validator = av.Alvalidator(params)

    color_range_from = validator.string_validate(params[0], 'Od')
    color_range_to = validator.string_validate(params[1], 'Do')
    if validator.evaluate() is False:
        return validator.filters_description

    for y in range(0, img.__len__()):
        for x in range(0, img[0].__len__()):
            if img[y][x][0] > color_range_from or img[y][x][0] < color_range_to:
                img[y][x][1] = 0

    return img

def equalize(img, params):
    '''Ekvalizace jasu'''

    #for x in range(0, len(img)):
    #    for y in range(0, len(img[0])):
    #        img[x][y] = 255 - img[x][y]
    validator = av.Alvalidator(params)

    if validator.evaluate() is False:
        return validator.filters_description
    #h, w = img.shape

    return cv2.equalizeHist(img)

def invert(img, params):
    '''Inverze jasu'''

    #for x in range(0, len(img)):
    #    for y in range(0, len(img[0])):
    #        img[x][y] = 255 - img[x][y]
    validator = av.Alvalidator(params)

    if validator.evaluate() is False:
        return validator.filters_description
    #h, w = img.shape

    img = 255 - img
    return img