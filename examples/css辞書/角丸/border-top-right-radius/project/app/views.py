from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from django.views import generic
from .forms import CssForm

d = z()
d["mode"] = "index"

def index(request):
    if request.method=="POST":
          f=CssForm(request.POST)
          if f.is_valid():
                 d["form"]=f
                 unit=f.fields["unit"].choices[int(f.cleaned_data["unit"])][1]+" "
                 ddd=" "+str(f.cleaned_data["value1"])+unit+str(f.cleaned_data["value5"])+unit
                 print (ddd)
                 with open("app/static/app/base_origin.css", "r") as ff:
                       data = ff.read()
                       data1=data.replace("--**__**", ddd)
                 with open("app/static/app/base.css", "w") as ff:
                       ff.write(data1)
                 return render(request, "app/index.html", d)
    else:
          initial={"value1":20,"value5":20,"unit":2, }
          f=CssForm(initial)
          d["form"]=f
    return render(request, "app/index.html", d)      


    