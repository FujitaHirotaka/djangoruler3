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
from django.views.decorators.http import require_POST

d=z()
d["mode"]="index"


def index(request):
    print(Player.team.field.__dict__)    
    print("")
    print(Player.title.field.__dict__)    
    print("")
    print(Player.title.field.verbose_name)
    print("")    
    print(Player.title.field.choices)    
    print("")    
    print((Player.gender.field_name)    )
    print("")    
    print((Player.gender.__dict__)    )
    print("")    
    d["player"]=Player
    return render(request, "app/index.html", d)

    

