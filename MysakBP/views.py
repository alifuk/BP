from django.http import HttpResponse
import os
from django.shortcuts import render
import importlib

import json
import numpy as np
import cv2
import time

import MysakBP.local_settings

operation_files = {}


def find_files():
    start = time.time()
    for file in os.listdir(MysakBP.local_settings.OPERATIONS_PATH):
        name = os.path.splitext(os.path.basename(file))[0]
        # add package prefix to name, if required
        operation_files[name] = importlib.import_module(MysakBP.local_settings.OPERATIONS_PATH_MODULE + name)

    end = time.time()
    # print(end - start)
    # search takes 0.04 on SSD drive


def uploadImage(request):
    if request.method == "POST":
        if request.FILES['fileToUpload']:
            img = cv2.imread(request.FILES['fileToUpload'].temporary_file_path())
            image_name = request.FILES['fileToUpload'].name
            image_name = image_name.replace('upload', '')
            cv2.imwrite(MysakBP.local_settings.STATIC_PATH + 'upload_' + image_name, img)
    else:
        return HttpResponse('Nenahráno' + os.getcwd())

    return HttpResponse('Nahráno' + os.getcwd())


def count(request, question_id):
    return HttpResponse('Eeeej' + question_id)


def saveThimbnailImage(img_to_write, operation_counter):
    cv2.imwrite(MysakBP.local_settings.STATIC_PATH + 'thumb_' + str(operation_counter) + '.png', img_to_write)


def work(request):
    find_files()

    img = np.zeros((10, 10, 3), np.uint8)

    json_data = json.loads(request.body)

    operation_counter = 0
    for arr_of_definition in json_data:

        if arr_of_definition[0] in operation_files:
            operation_pointer = getattr(operation_files[arr_of_definition[0]], arr_of_definition[1])
            img = operation_pointer(img, arr_of_definition[2:])
            saveThimbnailImage(img, operation_counter)
            operation_counter += 1
    return HttpResponse(os.getcwd())


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
