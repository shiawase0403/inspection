from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import reverse #反向解析
from django.urls import resolve #反向解析
from django.shortcuts import redirect #重定向
from .forms import *
from .models import *

# Create your views here.

def index(request):
    #GET请求
    if request.method == 'GET':
        v = maininspectionForm()
        return render(request, 'index.html', locals())
    # POST请求
    else:
        v = maininspectionForm(request.POST)
        if v.is_valid():
            id = request.GET.get('id')
            result = Dorminspect.objects.filter(id=id)
            if not result:
                v.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            # 获取错误信息，并以json格式输出
            error_msg = v.errors.as_json()
            print(error_msg)
            return render(request, 'index.html', locals())


