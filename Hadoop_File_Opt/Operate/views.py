from django.shortcuts import render
from django.shortcuts import HttpResponse
from Operate import tasks

# Create your views here.
def index(request):
    return render(request,'index.html')

def UpLoad(request):
    return render(request, "number.html")
