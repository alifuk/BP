"""Soubory"""
import cv2
import MysakBP.local_settings
import numpy as np
import MysakBP.views as v
import MysakBP.Model.Alvalidator as av

def load(img, params):
    '''
        Load image
        '''
    validator = av.Alvalidator(params)
    filename = validator.string_validate(params[0], 'Název souboru')
    if validator.evaluate() is False:
        return validator.filters_description

    img = cv2.imread(MysakBP.local_settings.STATIC_PATH + v.user_folder + '/' + filename)
    if str(img) != 'None':
        return img
    else:
        return np.zeros((10, 10, 3), np.uint8)


def save(img, params):
    '''
    Save image
    '''
    filename = params[0]
    try:
        cv2.imwrite(MysakBP.local_settings.STATIC_PATH + v.user_folder + '/generated_' + filename, img)
    except:
        print('Soubor neuložen')
    return img
