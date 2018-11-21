from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.views.decorators.http import require_POST
from . import forms



class Tashizan(View):
    initials={"char1":"適当", "check":True}
    d=z() 
    d["mode"]="index"
    form_class=forms.Form
    template_name="app/index.html"
    def get(self, request, *args, **kwargs):
         self.d["form"]=self.form_class(self.initials)
         return render(request, self.template_name, self.d)





