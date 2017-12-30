import cv2

def bw(img, params):
    for y in range(0, img.__len__()):
        for x in range(0, img[0].__len__()):
            img[y][x][1] = 0

    return img



def blue(img, params):
    for y in range(0, img.__len__()):
        for x in range(0, img[0].__len__()):
            if img[y][x][0] < 100 or img[y][x][0] > 150:
                img[y][x][1] = 0

    return img
