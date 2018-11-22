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
    latest_team_list=Teams.objects.order_by("-pub_date")[:5]
    output=",".join([i.name for i in latest_team_list])
    return HttpResponse(output)