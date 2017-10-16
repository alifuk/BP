from multiprocessing import context

from django.http import HttpResponse
from django.conf import settings
import numpy
import cv2
import time
import os
from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage


def index(request):
    print('aaa')
    if request.method == "POST":
        print('bb')
        if request.FILES['fileToUpload']:
            print(request.FILES['fileToUpload'].size)

            #img = request.FILES['fileToUpload']


            img = cv2.imread(request.FILES['fileToUpload'].temporary_file_path(),0)
            #cv2.imshow('image', img)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            cv2.imwrite('MysakBP/static/WTBW.png', img)


    ali = os.getcwd();
    #img = 'WTBW.png'
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
