from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from .models import Player
d=z()
d["mode"]="index"

def index(request):
    maru=Player(name="丸佳浩", team="C")
    maru.save()
    print(maru.team)
    print(maru.get_team_display())
    d["maru"]=maru
    return render(request, "app/index.html", d)

