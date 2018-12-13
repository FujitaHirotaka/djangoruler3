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
                 choice_list=f.fields['value1'].choices
                 print(choice_list)
                 d["choice"]=choice_list[int(f.cleaned_data["value1"])][1]

                                                 
                 with open("app/static/app/base_origin.css", "r") as ff:
                       data = ff.read()
                       data1=data.replace("**__value1__**", d["choice"])

    

                 with open("app/static/app/base.css", "w") as ff:
                       ff.write(data1)
                 return render(request, "app/index.html", d)
    else:
          f=CssForm({"value1":0, })
          d["form"]=f
    return render(request, "app/index.html", d)      


    