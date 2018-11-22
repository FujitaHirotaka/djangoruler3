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
    Player.objects.all().delete()
    maru=Player(name="丸佳浩")
    maru.save()
    maru.name="菊池涼介"
    maru.save()
    print(Player.objects.all())
    return render(request, "app/index.html", d)

