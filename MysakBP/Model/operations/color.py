import cv2


def bw(img, params):
    '''
        To grayscale
        '''
    for y in range(0, img.__len__()):
        for x in range(0, img[0].__len__()):
            img[y][x][1] = 0

    return img


def fcr(img, params):
    '''
    Filter color range
    '''
    for y in range(0, img.__len__()):
        for x in range(0, img[0].__len__()):
            if img[y][x][0] < 100 or img[y][x][0] > 150:
                img[y][x][1] = 0

    return img


def convert(img, params):
    print('begin')
    colorspace_from = params[0]
    colorspace_to = params[1]
    try:
        conversion_name = getattr(cv2, 'COLOR_' + colorspace_from + '2' + colorspace_to)
        img = cv2.cvtColor(img, conversion_name)
        print('heres')
    except:
        print('wrong conversion')
        pass

    return img
