from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from .models import Player, Team
d=z()
d["mode"]="index"

def index(request):
    Player.objects.all().delete()
    Team.objects.all().delete()
    maru=Player.objects.create(name="丸佳浩")
    kikuchi=Player.objects.create(name="菊池涼介")
    sugano=Player.objects.create(name="菅野智之")
    sakamoto=Player.objects.create(name="坂本勇人")    
    giants=Team(name="巨人")
    giants.save()#これ重要
    giants.players.add(sugano)
    giants.players.add(sakamoto)    
    giants.players.add(maru)
    giants.save()
    print(giants.players.all())

    carp=Team.objects.create(name="広島")
    carp.players.add(maru)
    carp.players.add(kikuchi)
    carp.save()
    print(carp.players.all())
    print(maru.team_set.all())
    d["player_list"]=Player.objects.all()
    d["team_list"]=Team.objects.all()

    
    return render(request, "app/index.html", d)

