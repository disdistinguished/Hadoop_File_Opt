**Hadoop_File_Opt**

这是一个Django项目，直接下载运行，在运行之前启动hadoop

* 使用celery对hadoop文件进行操作分为下面五个步骤：
    * Django搭建
    * iview前端页面
    * 搭建Hadoop环境
    * 使用python对Hadoop文件进行操作
    * 使用celery对文件进行操作

##Django搭建

创建一个Hadoop_File_Opt项目

```
django-admin startproject Hadoop_File_Opt
```

运行看是否创建成功

```
python manage.py runserver
```

再创建一个app

```
python manage.py startapp Operate
```
celery的配置

```
app = Celery('task',
             broker='redis://localhost',
             backend='redis://localhost')
             #配置redis
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hadoop_File_Opt.settings')
#设置环境变量，让celery知道项目的环境变量 
app = Celery('Hadoop_File_Opt')
#配置Django，Hadoop_File_Opt为当前工程

app.config_from_object('django.conf:settings', namespace='CELERY')
#在setting可以创建一个celery的命名空间 

app.autodiscover_tasks()
#自动发现app里面的selery任务

```


