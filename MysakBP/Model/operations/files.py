import cv2
import MysakBP.local_settings
import numpy as np

def load(img, params):
    '''
        Load image
        '''
    filename = params[0]
    img = cv2.imread(MysakBP.local_settings.STATIC_PATH + filename)
    if str(img) != 'None':
        return img
    else:
        return np.zeros((10, 10, 3), np.uint8)


def save(img, params):
    '''
    Save image
    '''

    filename = params[0]
    cv2.imwrite(MysakBP.local_settings.STATIC_PATH + filename, img)
    return img
