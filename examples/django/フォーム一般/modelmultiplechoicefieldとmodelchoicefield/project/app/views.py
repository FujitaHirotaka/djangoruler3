from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from django.views import generic
from .models import *
from .forms import PlayerForm, TIME_CHOICES
from django.views.decorators.http import require_POST
d=z()
d["mode"]="index"


def index(request):
    f=PlayerForm()
    d["form"]=f
    print(TIME_CHOICES)
    return render(request, "app/index.html", d)
 
 
@require_POST
def save(request):
    f = PlayerForm(request.POST)

    if f.is_valid():
        print(f.cleaned_data)
        title=f.cleaned_data["Title"]
        name=f.cleaned_data["name"]
        gender=f.cleaned_data["gender"]        
        login=f.cleaned_data["login"]
        team=f.cleaned_data["Team"]
        p=Player(name=name, gender=gender, login=login, team=team)
        p.save()
        p.title.set(title)
        p.save()
        return redirect('app:index')
 
    d["form"]=f
    return render(request, 'app/index.html', d)


    

