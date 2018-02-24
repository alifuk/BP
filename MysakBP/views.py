from django.http import HttpResponse
import os
from os import walk
from django.shortcuts import render
from django.shortcuts import redirect

import importlib

import json
import numpy as np
import cv2
import time
import hashlib
import random
import types

import threading

import MysakBP.local_settings

operation_files = {}
operation_files_description = {}
user_folder = ''


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
    if request.method == "POST" and 'fileToUpload' in request.FILES:
        img = cv2.imread(request.FILES['fileToUpload'].temporary_file_path())
        image_name = request.FILES['fileToUpload'].name
        image_name = image_name.replace('upload', '')
        cv2.imwrite(MysakBP.local_settings.STATIC_PATH + request.POST['user'] + '/upload_' + image_name, img)
    else:
        return HttpResponse('Nenahráno' + os.getcwd())

    return HttpResponse('Nahráno' + os.getcwd())


def saveThimbnailImage(img_to_write, operation_counter):
    # TODO aby obrázky který se lišej od poslední iterace se zapsali do nějakýho listu kterej se pošle na front
    global user_folder
    #width, height, depth = img_to_write.shape
    #if type(img_to_write) ==

    if type(img_to_write) is not list:

        cv2.imwrite(MysakBP.local_settings.STATIC_PATH + user_folder + '/thumb_' + str(operation_counter) + '.jpg',
                img_to_write)


def deleteAllThumbnailImages():
    global user_folder
    for filename in os.listdir(MysakBP.local_settings.STATIC_PATH + user_folder):
        if 'thumb' in filename:
            os.remove(MysakBP.local_settings.STATIC_PATH + user_folder + '/' + filename)



def work(request):



    find_files()
    img = np.zeros((10, 10, 3), np.uint8)

    json_data = json.loads(request.body)
    global user_folder
    user_folder = json_data[0][0]

    #with open(MysakBP.local_settings.STATIC_PATH + user_folder + '/last_work.json', 'w') as file:
    #    file.write(str(request.body))

    deleteAllThumbnailImages()
    operation_counter = 0
    for arr_of_definition in json_data[1:]:

        if arr_of_definition[0] in operation_files:
            operation_pointer = getattr(operation_files[arr_of_definition[0]], arr_of_definition[1])
            img = operation_pointer(img, arr_of_definition[2:])
            saveThimbnailImage(img, operation_counter)
            operation_counter += 1
    return HttpResponse(os.getcwd())




def layout(request, user):
    path = MysakBP.local_settings.STATIC_PATH + user
    if not os.path.exists(path):
        return redirect('login')

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


def getFiles(request, user):

    '''
    f = []
    for filename in os.listdir(MysakBP.local_settings.STATIC_PATH + user):
        if 'thumb' not in filename and 'last_work' not in filename:
            f.append(filename)


    return HttpResponse(json.dumps(f))

    '''


    global mythreads
    if 'mythreads' not in globals():
        mythreads = {}

    if user in mythreads:
        print('job již spuštěn')
    else:
        mythreads[user] = threading.Thread(target=job)
        mythreads[user].start()
        mythreads[user].join()
        mythreads.pop(user)
        print('done')
    #job()



    return HttpResponse('somethingg')

def job():

    print('Starting job')
    start = time.perf_counter()
    print(threading.get_ident())
    for i in range(1,100000000):
        k = 9
    end = time.perf_counter()
    print('job done in ' + str(end-start))
    return

def nothing():
    return

def getSavedCommand(request, user):
    with open(MysakBP.local_settings.STATIC_PATH + user + '/last_work.json', 'r') as file:
        last_command = file.read()
    return HttpResponse('{}')
    return HttpResponse(last_command)

def deleteFile(request):
    jsonovitch = json.loads(request.body)
    myfile = MysakBP.local_settings.STATIC_PATH + '/' + jsonovitch[0] + '/' + jsonovitch[1];
    if os.path.isfile(myfile):
        os.remove(myfile)

    return HttpResponse('ok')


def getAllOperationsWithParameters(request):


    start = time.time()
    test_params = ['get_validation_params', 'get_validation_params', 'get_validation_params', 'get_validation_params',
                   'get_validation_params', 'get_validation_params']

    for file in os.listdir(MysakBP.local_settings.OPERATIONS_PATH):
        if file == '__pycache__':
            continue
        name = os.path.splitext(os.path.basename(file))[0]
        module_import = importlib.import_module(MysakBP.local_settings.OPERATIONS_PATH_MODULE + name)
        operations = {}
        for function_in_module in dir(module_import):
            if isinstance(module_import.__dict__.get(function_in_module), types.FunctionType):
                pointer_to_function = getattr(module_import, function_in_module)
                operations[function_in_module] = {
                    'name': pointer_to_function.__doc__,
                    'short': function_in_module,
                    'params': pointer_to_function([], test_params)

                }

        operation_files_description[name] = {'name': module_import.__doc__,
                                             'operations': operations
                                             }

    end = time.time()
    return HttpResponse(json.dumps(operation_files_description))


def login(request):
    text = str(random.random())
    text = text.encode()
    something_random = hashlib.sha224(text).hexdigest()

    if 'static_path' in request.COOKIES:
        if os.path.exists(MysakBP.local_settings.STATIC_PATH + request.COOKIES['static_path']):
            return redirect('./' + request.COOKIES['static_path'])

    static_path = MysakBP.local_settings.STATIC_PATH + something_random
    if not os.path.exists(static_path):
        os.makedirs(static_path)

        img = cv2.imread(MysakBP.local_settings.STATIC_PATH + '/example_1.jpeg')
        cv2.imwrite(static_path + '/example_1.jpeg', img)
        img = cv2.imread(MysakBP.local_settings.STATIC_PATH + '/example_2.jpeg')
        cv2.imwrite(static_path + '/example_2.jpeg', img)
        img = cv2.imread(MysakBP.local_settings.STATIC_PATH + '/example_3.jpeg')
        cv2.imwrite(static_path + '/example_3.jpeg', img)


    else:
        return redirect('.')
    return redirect('./' + something_random)
