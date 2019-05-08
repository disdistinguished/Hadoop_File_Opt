from django.shortcuts import render
from django.shortcuts import HttpResponse
from Operate import tasks
from pyhdfs import HdfsClient
import os


# Create your views here.
def index(request):
    return render(request,'index.html')

def UpLoad(request):
    '''
    文件上传
    '''

    message = {}
    # lient=HdfsClient(hosts='localhost:50070')
    # # #连接到hdfs
    file = request.POST['q']
    # #接受网页提交的文件名
    # h_file = ('/tmp/te/%s'%file)
    # tasks.Copy_From_Local.delay(file)
    # #使用celery上传文件
    # if client.exists(h_file):
    #     message['res'] = 'UpLoad success'
    # else:
    #     message['res'] = 'Upload fail'
    # #判读是否上传成功，返回结果
    # res = tasks.add.delay(228,24)
    # print(res)
    message['res_u'] = 'UpLoad success'
    print(file)
    return render(request, "index.html",message)

def DownLoad(request):
    '''
    文件下载
    '''
    message = {}
    # file = request.POST['q']
    # #接受网页提交的文件名
    # tasks.Copy_To_Local.delay(file)
    # #使用celery下载文件
    # if os.path.exists(file):
    #     message['res'] = 'Download success'
    # else:
    #     message['res'] = 'Download fail'
    # #判读是否下载成功，返回结果
    message['res_d'] = 'Download fail'
    return render(request, "index.html",message)

