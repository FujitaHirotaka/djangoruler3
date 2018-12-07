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
                 source="images/"+os.path.basename(f.cleaned_data["source"])
                 slice=str(f.cleaned_data["slice"])
                 width=str(f.cleaned_data["width"])
                 outset=str(f.cleaned_data["outset"])
                 choice_list=f.fields['repeat'].choices
                 print(choice_list)
                 repeat=choice_list[int(f.cleaned_data["repeat"])][1]
     
                 with open("app/static/app/base_origin.css", "r") as ff:
                       data = ff.read()
                       data1=data.replace("**__source__**", source)
                       data1=data1.replace("**__slice__**", slice)
                       data1=data1.replace("**__width__**", width)
                       data1=data1.replace("**__outset__**", outset)
                       data1=data1.replace("**__repeat__**", repeat)                                              
                 with open("app/static/app/base.css", "w") as ff:
                       ff.write(data1)
                 return render(request, "app/index.html", d)
    else:
          f=CssForm({"slice":15, "width":15, "outset":15, "repeat":1 })
          d["form"]=f
    return render(request, "app/index.html", d)      


    