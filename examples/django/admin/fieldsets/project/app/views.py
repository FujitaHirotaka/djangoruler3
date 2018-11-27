from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse

d=z()
d["mode"]="index"

def index(request):
    return render(request, "app/index.html", d)

