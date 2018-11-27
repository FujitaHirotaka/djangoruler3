from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
import subprocess
from pathlib import Path
import psutil
import re


def ajax(request):
    cmd="taskkill /f /T /im chromedriver.exe"
    subprocess.Popen(cmd,shell=True)
    return HttpResponse("")


def ajax2(request):
    filepath=request.GET.get("filepath")
    text=""
    with open(filepath, "r",encoding="utf-8_sig") as f:
           for i in f.readlines():
                text+=i
    d={"text": text, "title":filepath}

    return JsonResponse(d)



def z():
    base_path = Path.cwd()
    file_path_list=[]
    hierarchy_list=[]
    for i in base_path.glob("**/*"):
       if not ("ajax" in str(i)) and not ("migrations" in str(i)) and not ("rightside.html" in str(i)) and not ("footer.html" in str(i)) and not ("footer_origin.html" in str(i)) and not ("views2.py" in str(i)) and not (".vscode" in str(i)) and not ("db.sqlite" in str(i)) and not ("manage.py" in str(i)) and not ("__pycache__" in str(i)): 
           mojiretu=str(i).replace(str(base_path)+"\\","")
           find_list=re.findall("\\\\", mojiretu) #ここ重要
           for ii in range(len(find_list)):
               mojiretu=mojiretu.replace("\\", "/")
           file_path_list.append(mojiretu)
           hierarchy_list.append(len(find_list))
    max_hierarchy_number=max(hierarchy_list)
    d={"file_path_list": file_path_list, "max_hierarchy_number":max_hierarchy_number}
    return d
