from multiprocessing import context
from django.http import HttpResponse
from django.conf import settings
import time
import os
from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage

import numpy as np
import cv02


def index(request):
    print('aaa')
    if request.method == "POST":
        print('bb')
        if request.FILES['fileToUpload']:
            print(request.FILES['fileToUpload'].size)

            # img = request.FILES['fileToUpload']


            img = cv02.imread(request.FILES['fileToUpload'].temporary_file_path())
            # cv2.imshow('image', img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            hsv = cv02.cvtColor(img, cv02.COLOR_BGR2HSV)

            # define range of blue color in HSV
            lower_blue = np.array([110, 50, 50])
            upper_blue = np.array([130, 255, 255])

            # Threshold the HSV image to get only blue colors
            mask = cv02.inRange(hsv, lower_blue, upper_blue)

            # Bitwise-AND mask and original image
            res = cv02.bitwise_and(img, img, mask=mask)
            cv02.imwrite('MysakBP/static/WTBW.png', mask)

    ali = os.getcwd();
    # img = 'WTBW.png'
    img = ('WTBW.png')
    dbg = []
    context = {
        'cisla': [1, 2, 3, 5, 7],
        'foto': img,
        'debug': dbg,
        'time': round(time.time())

    }

    return render(request, 'index.html', context)


def count(request, question_id):
    return HttpResponse('Eeeej' + question_id)


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

    maxHue = np.argmax(hues)
    o = 0
    x1 =50
    y1=50
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

        for y in range(y1-50, y2+50 ):
            for x in range(x1-50, x2+50 ):
                if abs(bgr[y][x][0] - maxHue) < 2:
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
        o+=1
        print(o)

        video.write(bgr)
        if o == 200 :
            break

    video.release()
    return HttpResponse('Eeeej')


def show():
    cv02.imshow('Image', bgr)
    cv02.waitKey(0)
    return True
