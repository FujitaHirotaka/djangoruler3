from django.shortcuts import render
import os
from .forms import *
from pathlib import Path
import re


def index(request):
    #ここの部分は本編とは関係ない
    file_path_list=make_file_path_list()[0]
    hierarchy_list=make_file_path_list()[1]
    max_hierarchy_number=max(hierarchy_list)
    
    #変数、file_path_list、max_hierarch_numberは本編とは関係ない
    return render(request, 'app/index.html', {"form": Form, "form2": Form2,"form3": Form3,"form4": Form4,"form5": Form5,"file_path_list": file_path_list, "max_hierarchy_number":max_hierarchy_number})



#ここから下は本篇とは関係ない

def make_file_path_list():
    base_path = Path.cwd()
    file_path_list=[]
    hierarchy_list=[]
    for i in base_path.glob("**/*"):
       if not ("migrations" in str(i)) and not ("rightside.html" in str(i)) and not ("footer.html" in str(i)) and not ("footer_origin.html" in str(i)) and not ("views2.py" in str(i)) and not (".vscode" in str(i)) and not ("db.sqlite" in str(i)) and not ("manage.py" in str(i)) and not ("__pycache__" in str(i)): 
           mojiretu=str(i).replace(str(base_path)+"\\","")
           find_list=re.findall("\\\\", mojiretu) #ここ重要
           for ii in range(len(find_list)):
               mojiretu=mojiretu.replace("\\", "/")
           file_path_list.append(mojiretu)
           hierarchy_list.append(len(find_list))
    return file_path_list, hierarchy_list


