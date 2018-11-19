from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.views.decorators.http import require_POST
from . import forms



class Tashizan(View):
    initial_numbers={"number1":1, "number2":2}
    d=z() 
    d["mode"]="index"
    d["form1"]=forms.Form(initial_numbers)
    template_name="app/index.html"
    form_class2=forms.Form2
    def get(self, request, *args, **kwargs):
         self.d["form2"]=self.form_class2(self.initial_numbers)
         return render(request, self.template_name, self.d)
    def post(self, request, *args, **kwargs):
         form2=self.form_class2(request.POST)
         if form2.is_valid():
             e=form2.cleaned_data
             a=form2.cleaned_data["number1"]
             b=form2.cleaned_data["number2"]
             c=a+b
             e["number3"]=c
             self.d["form2"]=self.form_class2(e)
         return render(request, self.template_name, self.d)


class Result(View):
    d=z() 
    d["mode"]="result"
    def post(self, request, *args, **kwargs):
       form1=forms.Form(request.POST)
    #request.POSTで受け取る場合
       if form1.is_valid():
          a1=request.POST["number1"]
          b1=request.POST["number2"]
          c1=a1+b1
          self.d["c1"]=c1
    #form.cleaned_dataで受け取る場合
       if form1.is_valid():
          a=form1.cleaned_data["number1"]
          b=form1.cleaned_data["number2"]
          c=a+b
          self.d["c"]=c
       return render(request, "app/index.html", self.d)    
    

