from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from .models import Teams, Players
from django.utils import timezone

def index(request,max_hierarchy_number, file_path_list, mode):
    Teams.objects.filter(name="巨人").delete()
    Players.objects.filter(name="丸佳浩").delete()
    Players.objects.filter(name="松山竜平").delete()    
    print(Teams.objects.all())
    giants = Teams(name="巨人", pub_date=timezone.now())
    #giants.save()をしないとデータベースに書き込まれない。
    giants2=Teams.objects.filter(name="巨人")
    if giants2:
        print("巨人はデータベースにすでに存在します。")
    else:
        giants.save()
    print(Teams.objects.all())
    giants=Teams.objects.get(name="巨人")
    print(giants.id)
    print(giants.name)
    print(giants.pub_date)
    print(Teams.objects.get(name__startswith="巨"))
    print(Players.objects.all())
    maru=Players(name="丸佳浩", team=giants)
    maru2=Teams.objects.filter(name="丸佳浩")
    if maru2:
        print("丸佳浩はデータベースにすでに存在します。")
    else:
        maru.save()
    print(maru.id)    
    print(maru.pk)        
    print(maru.name)
    print(maru.team)
    print(maru.team.id)
    print(maru.team.name)
    print(maru.team.pub_date)
    print(maru.team.was_published_recently())
    giants.players_set.create(name="松山竜平")
    print(giants.players_set.all())
    print(giants.players_set.count())    
    print(giants.pub_date.year)
    print(Teams.objects.filter(pub_date__year=timezone.now().year))



    return HttpResponse("OK")