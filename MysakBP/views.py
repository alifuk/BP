from multiprocessing import context
from django.http import HttpResponse
from django.conf import settings
import time
import os
from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage

import numpy as np
import cv2


def color_bw(img):
    for y in range(0, img.__len__()):
        for x in range(0, img[0].__len__()):
            img[y][x][1] = 0

    return img


def color_blue(img):
    for y in range(0, img.__len__()):
        for x in range(0, img[0].__len__()):
            if img[y][x][0] < 100 or img[y][x][0] > 150:
                img[y][x][1] = 0

    return img


def transform_rotate(img):
    rows, cols, channels = img.shape

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))

    return dst


def transform_crop(img):
    return cv2.resize(img, None, fx=4, fy=2, interpolation=cv2.INTER_CUBIC)


def filter_smooth(img):
    kernel = np.ones((10, 10), np.float32) / 100
    return cv2.filter2D(img, -1, kernel)

def uploadImage(request):
    if request.method == "POST":
        if request.FILES['fileToUpload']:
            print(request.FILES['fileToUpload'].size)

            # img = request.FILES['fileToUpload']

            img = cv2.imread(request.FILES['fileToUpload'].temporary_file_path())


            try:
                cv2.imwrite('./static/original.png', img)
            except:
                cv2.imwrite('./BP/MysakBP/static/original.png', img)
    else:
        return HttpResponse('Nenahráno' + os.getcwd())

    ali = os.getcwd()


    return HttpResponse('Nahráno' + os.getcwd())


def count(request, question_id):
    return HttpResponse('Eeeej' + question_id)


def loadImage():
    try:
        return cv2.cvtColor(cv2.imread('./static/original.png', -1), cv2.COLOR_BGR2HSV)
    except:
        return cv2.cvtColor(cv2.imread('./BP/MysakBP/static/original.png', -1), cv2.COLOR_BGR2HSV)


def saveImage(imgToWrite):
    # cv2.imshow('image',  cv2.cvtColor(imgToWrite, cv2.COLOR_HSV2BGR))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    cv2.imwrite('./static/final.png', cv2.cvtColor(imgToWrite, cv2.COLOR_HSV2BGR))


def work(request):
    img = loadImage()
    for key, value in request.POST.items():

        if key == 'color_bw':
            img = color_bw(img)

        if key == 'color_blue':
            img = color_blue(img)

        if key == 'transform_rotate':
            img = transform_rotate(img)

        if key == 'transform_crop':
            img = transform_crop(img)

        if key == 'filter_smooth':
            img = filter_smooth(img)


    saveImage(img)
    return HttpResponse('ok')


def layout(request):
    dbg = []
    source_foto = ('./original.png')
    final_foto = ('./final.png')
    context = {
        'final_foto': final_foto,
        'source_foto': source_foto,
        'debug': dbg,
        'time': round(time.time())

    }
    return render(request, 'index.html', context)


def init(request):
    print('SDF')
    from multiprocessing import context
    from django.http import HttpResponse
    from django.conf import settings
    import time
    import os
    from django.shortcuts import render
    from django.contrib.staticfiles.storage import staticfiles_storage

    import numpy as np
    import cv2

    video = cv2.VideoWriter('video.avi', -1, 25, (640, 480))
    cap = cv2.VideoCapture('cv02_hrnecek.mp4')
    hues = []
    track = cv2.imread('cv02_vzor_hrnecek.bmp')
    track = cv2.cvtColor(track, cv2.COLOR_RGB2HSV)
    for i in range(0, 255):
        hues.append(0)

    for y in range(0, track.__len__()):
        for x in range(0, track[0].__len__()):
            hues[track[y][x][0]] += 1

    maxHue = max(hues)
    maxHueIndex = np.argmax(hues)
    o = 0
    x1 = 50
    y1 = 50
    y2 = 400
    x2 = 500
    while True:
        print('while')
        ret, bgr = cap.read()
        print(ret)
        if not ret:
            break

        bgr = cv2.cvtColor(bgr, cv2.COLOR_RGB2HSV)

        huesX = []
        for i in range(0, bgr.__len__()):
            huesX.append(0)

        huesY = []
        for i in range(0, bgr[0].__len__()):
            huesY.append(0)

        for y in range(y1 - 50, y2 + 50):
            for x in range(x1 - 50, x2 + 50):
                if abs(bgr[y][x][0] - maxHueIndex) < 2:
                    huesX[y] += 1
                    huesY[x] += 1

        sumx = 0
        sum = 0
        for k in range(0, huesX.__len__()):
            sumx += k * huesX[k]
            sum += huesX[k]

        maxHueY = round(sumx / sum)

        sumy = 0
        sum = 0
        for k in range(0, huesY.__len__()):
            sumy += k * huesY[k]
            sum += huesY[k]

        maxHueX = round(sumy / sum)

        x1 = round(maxHueX - track[0].__len__() / 2)
        y1 = round(maxHueY - track.__len__() / 2)
        x2 = round(maxHueX + track[0].__len__() / 2)
        y2 = round(maxHueY + track.__len__() / 2)

        cv2.rectangle(bgr, (x1, y1), (x2, y2), (122, 255, 0))
        bgr = cv2.cvtColor(bgr, cv2.COLOR_HSV2RGB)
        o += 1
        print(o)

        video.write(bgr)
        if o == 200:
            break

    video.release()
    return HttpResponse('Eeeej')


def cal():
    import numpy as np
    import cv2
    mask = cv2.imread('sc1.png')
    mask = cv2.cvtColor(mask, cv2.COLOR_RGB2HSV)
    sc = cv2.imread('sc2.png')
    sc = cv2.cvtColor(sc, cv2.COLOR_RGB2HSV)
    for y in range(0, sc.__len__()):
        for x in range(0, sc[0].__len__()):
            sc[y][x][2] += 128 - mask[y][x][2]

    sc = cv2.cvtColor(sc, cv2.COLOR_HSV2RGB)
    cv2.imwrite('sc3.png', sc)


def equaliz():
    import numpy as np
    import cv2
    mask = cv2.imread('cv04_rentgen.bmp')
    mask = cv2.cvtColor(mask, cv2.COLOR_RGB2HSV)
    values = []
    hues = []
    for i in range(0, 255):
        values.append(0)
        hues.append(0)
    for y in range(0, mask.__len__()):
        for x in range(0, mask[0].__len__()):
            values[mask[y][x][0]] += 1

    sum = 0
    for i in range(0, 255):
        sum += values[i]

    counter = 0
    for i in range(0, 255):
        counter += values[i]
        values[i] = 255 / (mask.__len__() * mask[0].__len__()) * counter

    for y in range(0, mask.__len__()):
        for x in range(0, mask[0].__len__()):
            mask[y][x][2] += values[mask[y][x][2]]

    mask = cv2.cvtColor(mask, cv2.COLOR_HSV2RGB)
    cv2.imwrite('sc4.png', mask)


def rotate():
    import numpy as np
    import cv2

    img = cv2.imread('sc2.png', 0)
    rows, cols = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 1)
    print(M)
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imwrite('sc4.png', dst)


def myscale():
    import numpy as np
    import cv2
    from numpy.linalg import inv

    img = cv2.imread('sc5.png')
    rows = img.__len__()
    cols = img[0].__len__()
    rows = rows * 1
    cols = cols * 1
    blank_image = np.zeros((cols, rows, 3), np.uint8)

    for x in range(0, cols):
        for y in range(0, rows):
            a = [x, y]
            b = [[2, 0], [0, 1.2]]
            b = inv(b)
            c = np.dot(a, b)

            blank_image[x][y] = img[int(c[0])][int(c[1])]

    cv2.imwrite('sc4.png', blank_image)


def myrotate():
    import numpy as np
    import cv2
    import math
    from numpy.linalg import inv

    img = cv2.imread('sc5.png')
    rows = img.__len__()
    cols = img[0].__len__()
    rows = rows * 1
    cols = cols * 1
    blank_image = np.zeros((cols, rows, 3), np.uint8)

    for x in range(0, cols):
        for y in range(0, rows):
            a = [x, y]
            b = [[math.cos(1), -math.cos(1)], [math.sin(1), math.cos(1)]]
            b = inv(b)
            c = np.dot(a, b)
            if int(c[0]) in range(0, cols) and int(c[1]) in range(0, rows):
                blank_image[x][y] = img[int(c[0])][int(c[1])]

    cv2.imwrite('sc4.png', blank_image)


def show():
    cv02.imshow('Image', bgr)
    cv02.waitKey(0)
    return True
