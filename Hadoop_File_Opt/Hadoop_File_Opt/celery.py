#!/usr/local/bin/python3

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
 
# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hadoop_File_Opt.settings')
 
app = Celery('Hadoop_File_Opt')
 

project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '%s.settings' % project_name
 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)
 

app = Celery(project_name)
# app.config_from_object('django.conf:settings', 'CELERY')
app.config_from_object('django.conf:settings')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hadoop_File_Opt.settings')
#设置环境变量，让celery知道项目的环境变量 
app = Celery('Hadoop_File_Opt')
#配置Django，Hadoop_File_Opt为当前工程
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '%s.settings' % project_name
#获取当前文件夹名，即为该Django的项目名 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)
#设置环境变量
app = Celery(project_name)
#实例化Celery
app.config_from_object('django.conf:settings')
#使用django的settings文件配置celery
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#自动发现app里面的selery任务
 
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))