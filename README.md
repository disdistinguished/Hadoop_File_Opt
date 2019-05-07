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
python manage.py startapp myapp
```

修改Django的配置文件view.py, url.py ,setting.py

```
#view.py添加
def index(request):
    return render(request,'index.html')
```

```
# url.py添加
urlpatterns = [
    url(r'^index',views.index),
]

```

