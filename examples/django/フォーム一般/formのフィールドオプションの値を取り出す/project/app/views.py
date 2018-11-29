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
from .forms import PlayerForm
from django.views.decorators.http import require_POST
d=z()
d["mode"]="index"


def index(request):
    f=PlayerForm()
    print(f.fields["title"].label)
    print((f.fields["team"].choices.queryset))      
    print(f.fields["name"].widget.attrs["class"])
    d["form"]=f
    return render(request, "app/index.html", d)
 
 

    

