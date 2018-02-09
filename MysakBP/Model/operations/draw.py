'''Vykreslení'''


import cv2
import MysakBP.Model.Alvalidator as av

def square(positions, params):
    '''Vykreslení tvaru'''

    validator = av.Alvalidator(params)
    img = validator.file_validate(params[0], 'Obraz do kterého se bude vykreslovat')
    if validator.evaluate() is False:
        return validator.filters_description

    v_c = 50

    for p in positions:

        #cv2.imwrite(str(counter) + ".jpg", original[p[0]-v_c: p[0] + v_c, p[1]-v_c:p[1]+v_c])
        cv2.rectangle(img, (p[1]-v_c, p[0]-v_c), (p[1] + v_c, p[0] + v_c), 255, 3)

    return img