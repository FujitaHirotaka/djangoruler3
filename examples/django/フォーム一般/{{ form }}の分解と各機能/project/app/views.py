from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.views.decorators.http import require_POST
from . import forms

class Index(View): 
  d=z()
  initial_data={"name":"<google>", "url":"http://google.co.jp"}   
  d["mode"]="index"  
  def get(self,request, *args, **kwargs):
    self.d["form1"]=forms.Form(self.initial_data)
    return render(request, "app/index.html", self.d)       
  def post(self,request, *args, **kwargs):
    form1=forms.Form(request.POST)   
    if form1.is_valid():
         self.d["form1"]=form1
    else:
         self.d["form1"]=form1
         print(form1.errors)
    return render(request, "app/index.html", self.d)         
