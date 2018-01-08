import cv2
import MysakBP.local_settings
import numpy as np
import MysakBP.views as v

def load(img, params):
    '''
        Load image
        '''
    filename = params[0]
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
