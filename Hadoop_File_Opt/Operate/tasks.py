from __future__ import absolute_import, unicode_literals
from celery import shared_task
from pyhdfs import HdfsClient
 
 
@shared_task
def Copy_From_Local(file):
    '''
    上传文件到hadoop
    '''
    h_file = ('/tmp/te/%s'%file)
    client=HdfsClient(hosts='localhost:50070')#hdfs地址
    if client.exists(h_file):
        client.delete(h_file)
    client.copy_from_local(file,h_file)
 
 
@shared_task
def Copy_To_Local(file):
    '''
    从Hadoop上下载文件
    '''
    client=HdfsClient(hosts='localhost:50070')#hdfs地址
    client.copy_to_local(file,'./')
 
 