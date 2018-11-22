from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse

def index(request,max_hierarchy_number, file_path_list, mode):
    aa="""
        <a href="http://127.0.0.1:8000/app/1678">detail</a><br>
        <a href="http://127.0.0.1:8000/app/3451/result/">result</a><br>
        <a href="http://127.0.0.1:8000/app/136/vote/">vote</a><br>"""
    return HttpResponse(aa)

def detail(request,max_hierarchy_number, file_path_list, mode, team_id):
    aa="ここはteam_id:{}(detail)".format(str(team_id))
    return HttpResponse(aa)

def result(request,max_hierarchy_number, file_path_list, mode, team_id):
    aa="ここはteam_id:{}(result)".format(str(team_id))
    return HttpResponse(aa)   
def vote(request,max_hierarchy_number, file_path_list, mode, team_id):
    aa="ここはteam_id:{}(vote)".format(str(team_id))
    return HttpResponse(aa)     