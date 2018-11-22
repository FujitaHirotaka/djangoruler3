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
from django.template import loader

d=z()
d["mode"]="index"
def index(request,max_hierarchy_number, file_path_list, mode):
    latest_team_list=Teams.objects.order_by("-pub_date")[:5]
    d['latest_team_list']= latest_team_list

    return render(request, "app/index.html", d)

def detail(request,max_hierarchy_number, file_path_list, mode, team):
    output="ここは{}のページ".format(team)
    return HttpResponse(output)    