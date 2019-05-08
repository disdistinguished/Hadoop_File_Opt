#!/usr/local/bin/python3

from django.shortcuts import render
from django.shortcuts import HttpResponse
from Operate import tasks
from pyhdfs import HdfsClient
import os


# Create your views here.
def index(request):
    return render(request,'index.html')

def UpLoad(request):
    message = {}
    # lient=HdfsClient(hosts='localhost:50070')
    file = request.POST['q']
    # h_file = ('/tmp/te/%s'%file)
    # tasks.Copy_From_Local.delay(file)
    # if client.exists(h_file):
    #     message['res'] = 'UpLoad success'
    # else:
    #     message['res'] = 'Upload fail'
    print("running task")
    res = tasks.add.delay(228,24)
    print("start running task")
    print(res)
    message['res_u'] = 'UpLoad success'
    print(file)
    return render(request, "index.html",message)

def DownLoad(request):

    message = {}
    # file = request.POST['q']
    # tasks.Copy_To_Local.delay(file)
    # if os.path.exists(file):
    #     message['res'] = 'Download success'
    # else:
    #     message['res'] = 'Download fail'
    message['res_d'] = 'Download fail'
    return render(request, "index.html",message)

