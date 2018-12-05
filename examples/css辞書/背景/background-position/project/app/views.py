from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from django.views import generic
from .forms import *

d = z()
d["mode"] = "index"

def index(request):
    if request.method=="POST":
          if "general" in str(request.POST["name"]):
             f=CssForm(request.POST)
             f1=CssForm_length()
             f2=CssForm_percentage()             
             if f.is_valid():
                 d["form"]=f
                 d["form1"]=f1
                 d["form2"]=f2
                 choice_list=f.fields['value'].choices
                 print(choice_list)
                 d["choice"]=choice_list[int(f.cleaned_data["value"])][1]
                 print (d["choice"])
                 with open("app/static/app/base_origin.css", "r") as ff:
                       data = ff.read()
                       data1=data.replace("--**__**", d["choice"])
                 with open("app/static/app/base.css", "w") as ff:
                       ff.write(data1)
                 return render(request, "app/index.html", d)
          elif "length" in  str(request.POST["name"]):    
             f=CssForm()
             f1=CssForm_length(request.POST)
             f2=CssForm_percentage()    
             if f1.is_valid():
                 d["form"]=f
                 d["form1"]=f1
                 d["form2"]=f2
                 d["choice"]=str(request.POST["width"])+"px "+str(request.POST["height"])+"px"
                 
                 with open("app/static/app/base_origin.css", "r") as ff:
                       data = ff.read()
                       data1=data.replace("--**__**", d["choice"])
                 with open("app/static/app/base.css", "w") as ff:
                       ff.write(data1)
                 return render(request, "app/index.html", d)  
          elif "percentage" in  str(request.POST["name"]):    
             f=CssForm()
             f1=CssForm_length()
             f2=CssForm_percentage(request.POST)    
             if f2.is_valid():
                 d["form"]=f
                 d["form1"]=f1
                 d["form2"]=f2
                 d["choice"]=str(request.POST["width"])+"% "+str(request.POST["height"])+"%"
                 
                 with open("app/static/app/base_origin.css", "r") as ff:
                       data = ff.read()
                       data1=data.replace("--**__**", d["choice"])
                 with open("app/static/app/base.css", "w") as ff:
                       ff.write(data1)
                 return render(request, "app/index.html", d)  

    else:
          f=CssForm()
          f1=CssForm_length()
          f2=CssForm_percentage()
          d["form"]=f
          d["form1"]=f1
          d["form2"]=f2
    return render(request, "app/index.html", d)      


    