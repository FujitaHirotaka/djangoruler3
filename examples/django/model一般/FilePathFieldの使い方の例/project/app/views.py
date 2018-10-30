from django.shortcuts import render
from django.http import HttpResponse
import os
from .forms import Form
import subprocess
from pathlib import Path

def index(request):
    base_path = Path.cwd()
    return render(request, 'app/index.html', {"form": Form})



def ajax(request):
    pid = request.GET.get("pid")
    cmd="taskkill /F /pid "+str(pid)
    print(cmd)
    subprocess.Popen(cmd,shell=True)
    return HttpResponse(pid)

