from django.shortcuts import render
from django.http import HttpResponse
import os
from .forms import Form
import subprocess
from pathlib import Path
import psutil
import re

def index(request):
    base_path = Path.cwd()
    file_path_list=[]
    hierarchy_list=[]
    for i in base_path.glob("**/*"):
       if not (".vscode" in str(i)) and not ("db.sqlite" in str(i)) and not ("manage.py" in str(i)) and not ("__pycache__" in str(i)): 
           mojiretu=str(i).replace(str(base_path)+"\\","")
           find_list=re.findall("\\\\", mojiretu) #ここ重要
           for ii in range(len(find_list)):
               mojiretu=mojiretu.replace("\\", "/")
           file_path_list.append(mojiretu)
           hierarchy_list.append(len(find_list))
    max_hierarchy_number=max(hierarchy_list)

    print(file_path_list)
    print(max_hierarchy_number)


    return render(request, 'app/index.html', {"form": Form, "file_path_list": file_path_list, "max_hierarchy_number":max_hierarchy_number})



def ajax(request):
    pid = request.GET.get("pid")
    pid_list=psutil.pids()

    if int(pid) in pid_list:
        cmd="taskkill /F /pid "+str(pid)
        subprocess.Popen(cmd,shell=True)

    return HttpResponse(pid)

