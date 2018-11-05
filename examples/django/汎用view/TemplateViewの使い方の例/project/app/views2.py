from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
import subprocess
from pathlib import Path
import psutil
import re


def ajax(request):
    pid = request.GET.get("pid")
    pid_list=psutil.pids()

    if int(pid) in pid_list:
        cmd="taskkill /f /T /im chromedriver.exe"
        subprocess.Popen(cmd,shell=True)

    return HttpResponse(pid)


def ajax2(request):
    filepath=request.GET.get("filepath")
    text=""
    with open(filepath, "r",encoding="utf-8_sig") as f:
           for i in f.readlines():
                text+=i
    d={"text": text, "title":filepath}

    return JsonResponse(d)