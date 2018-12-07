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
                 value1=str(f.cleaned_data["value1"])+"px"
                 value2=str(f.cleaned_data["value2"])+"px"
                 value3=str(f.cleaned_data["value3"])+"px"
                 value4=str(f.cleaned_data["value4"])+"px"
                 inset=f.cleaned_data["inset"]                                                        
                 with open("app/static/app/base_origin.css", "r") as ff:
                       data = ff.read()
                       data1=data.replace("**__value1__**", value1)
                       data1=data1.replace("**__value2__**", value2)
                       data1=data1.replace("**__value3__**", value3)
                       data1=data1.replace("**__value4__**", value4)
                       if inset:
                             data1=data1.replace("**__inset__**", "inset")
                       else:
                             data1=data1.replace("**__inset__**", "")      

                 with open("app/static/app/base.css", "w") as ff:
                       ff.write(data1)
                 return render(request, "app/index.html", d)
    else:
          f=CssForm({"value1":15, "value2":15, "value3":15, "value4":1, "inset": False })
          d["form"]=f
    return render(request, "app/index.html", d)      


    