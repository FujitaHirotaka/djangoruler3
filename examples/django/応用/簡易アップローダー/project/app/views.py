from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from .forms import FileForm
from .models import *
from django.views.decorators.http import require_POST

d=z()
d["mode"]="index"

def index(request):

    data = File.objects.latest("id")  # 結果的に最新のFileが得られる
    print(dir(data.file))
    print(data.file.path)
    print(data.file.name)
    print(data.file.url)
    print(data.file.file)    
    
    f=FileForm()
    d["all_data"]=File.objects.all()
    d["form"]=f
    return render(request, "app/index.html", d)


@require_POST
def save(request):
 
    f = FileForm(data=request.POST, files=request.FILES)
    if f.is_valid():
        f.save()

        return redirect("app:index")
    else:
        d["all_data"]= File.objects.all()
        d["form"]= f
        return render(request, 'app/index.html', d)    