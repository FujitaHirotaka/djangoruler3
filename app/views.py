from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound
import os
from pathlib import Path
from .forms import DjangoForm
from .models import *
import re



def get_project_list():
    judge_set = {"wsgi.py", "settings.py", "urls.py", "__init__.py"}
    directory_of_projects=Path(os.path.abspath(__file__)).parents[3]
    project_list=[]
    project_candidate_list=[i for i in directory_of_projects.glob("*") if i.is_dir()]
    for i in project_candidate_list:
        project_path=Path(directory_of_projects/i)
        name_list=[ii.name for ii in project_path.glob("*")]
        dir_list=[project_path/ii/ii for ii in name_list if (project_path/ii/ii).exists()]
        for ii in dir_list:
            file_list=[iii.name for iii in ii.glob("*")]
            if not (judge_set-set(file_list)):
                    project_list.append(i.name)
    project_list.remove("djangoruler")
    return project_list


project_list=get_project_list()


def main(request):
###新規プロジェクトを作る

###プロジェクトの選択###

    allproject_list=[i.project_name for i in DjangoProject.objects.all()]
    return render(request, "app/main.html", {"allproject_list":allproject_list})


def projectmake(request):
    project_name= request.POST.get("project_name")
    if re.match("^[a-zA-Z0-9_]+$", project_name):
        if re.match("^[A-Z]", project_name):
            project,created=DjangoProject.objects.get_or_create(project_name=project_name)
            return HttpResponse(project_name)
        else:
            return HttpResponse("プロジェクト名の始文字は大文字にする。プロジェクトを新しく作るか選びなおすボタンをおしてください。")
    else:
        return HttpResponse("エラー。プロジェクト名は英数字_のみ。プロジェクトを新しく作るか選びなおすボタンをおしてください。")


def projectselect(request):
    project_name= request.POST.get("project_select")
    #if project_name in project_list:
    project = DjangoProject.objects.get(project_name=project_name)
    return HttpResponse(project_name)
    #else:
    #    raise Exception("エラー。このプロジェクトは実際には存在しません")


def projectreturn(request):
    return redirect(reverse("app:main"))
