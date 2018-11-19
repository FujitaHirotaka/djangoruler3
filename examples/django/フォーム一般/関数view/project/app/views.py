from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.views.decorators.http import require_POST
from . import forms

d=z()

initial_numbers={"number1":1, "number2":2}
def tashizan(request):
    d["mode"]="index"
    d["form1"]=forms.Form(initial_numbers)
    if request.method=="POST":
         form2=forms.Form2(request.POST)
         if form2.is_valid():
              e=form2.cleaned_data
              a=form2.cleaned_data["number1"]
              b=form2.cleaned_data["number2"]
              c=a+b
              e["number3"]=c
              d["form2"]=forms.Form2(e)
    else:
         d["form2"]=forms.Form2(initial_numbers)
    return render(request, "app/index.html", d)

@require_POST
def result(request):
    d["mode"]="result"
    #request.POSTで受け取る場合
    a1=request.POST["number1"]
    b1=request.POST["number2"]
    c1=a1+b1
    d["c1"]=c1
    #form.cleaned_dataで受け取る場合
    form1=forms.Form(request.POST)
    if form1.is_valid():
        a=form1.cleaned_data["number1"]
        b=form1.cleaned_data["number2"]
        c=a+b
        d["c"]=c
    return render(request, "app/index.html", d)    
    

