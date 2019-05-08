#!/usr/local/bin/python3

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from pyhdfs import HdfsClient
import os
 
 
@shared_task
def Copy_From_Local(file):
    '''
    上传文件到hadoop
    '''
    h_file = ('/tmp/te/%s'%file)
    client=HdfsClient(hosts='localhost:50070')#hdfs地址，连接hdfs
    if client.exists(h_file):
        client.delete(h_file)
        #判断文件是否存在于hdfs，存在就删除
    client.copy_from_local(file,h_file)
    #从本地添加文件到hdfs
   
@shared_task
def Copy_To_Local(file):
    '''
    从Hadoop上下载文件
    '''
    client=HdfsClient(hosts='localhost:50070')#连接到hdfs
    if os.path.exists(file):
        os.remove(file)
        #判断本地是否存在文件，存在就删除
    client.copy_to_local(file,'./')
    