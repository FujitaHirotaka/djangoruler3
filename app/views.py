from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, JsonResponse
import shutil
import os
from pathlib import Path
from .forms import DjangoForm
from .models import *
import re
import subprocess
import time

directory_of_projects=Path("C://users/sakodaken/pycharmprojects") #Path(os.path.abspath(__file__)).parents[3] でもＯＫ

def get_project_list():
    """
    フォルダ構造を調べることにより、このアプリで作ったプロジェクトかどうかを判断し、そうであれば格納しリストとして返す関数。
    基本的には一つ下のフォルダ階層にproject名/project名のような階層を持ち、
    その中にwsgi.py、settings.py、urls.py、__init__.pyを持つかどうかでまずプロジェクトフォルダかどうかを判断。
　　さらに、settings.pyに"made_by_djangoruler2_app\n"が最初に記載されているかどうかを調べ、
   （なお、これについては、projectmakeのviewで書き込む）djangoruler2アプリで作られたものかどうかを判断。
    後者をやる理由は、このアプリで作った以外のプロジェクトである場合、プログラムの構造が想定とは異なり、
    このアプリがうまく機能するかわからないため。
    """
    judge_set = {"wsgi.py", "settings.py", "urls.py", "__init__.py"} #judge_set:プロジェクトのフォルダがあるかどうかを判断するための集合。以下の名前のファイルがあればプロジェクトフォルダと判断。
    project_list=[] #project_list:このアプリで作られたプロジェクトの名前を格納したリスト
    project_candidate_list=[i for i in directory_of_projects.glob("*") if i.is_dir()]
    for i in project_candidate_list:
        project_path=Path(directory_of_projects/i)
        name_list=[ii.name for ii in project_path.glob("*")]
        dir_list=[project_path/ii/ii for ii in name_list if (project_path/ii/ii).exists()]
        for ii in dir_list:
            file_list=[iii.name for iii in ii.glob("*")]
            if not (judge_set-set(file_list)):
                    project_list.append(i.name)

    ##settings.pyに"made_by_django_ruler2_app"が1行目に記載されているかを調べ、このアプリで作られたものかを判断
    project_list_sin=[]
    for i in project_list:
        settings_path=Path(directory_of_projects/i/"project"/"project"/"settings.py")
        if settings_path.exists():
            with open(os.path.join(directory_of_projects, i, "project", "project","settings.py"), "r") as f:
                sentence_list=f.readlines()
                if "made_by_djangoruler2_app" in sentence_list[0]:
                    project_list_sin.append(i)
    return project_list_sin

def get_project_list2(project_list):
   """
   get_project_listで得られるプロジェクトリストとデータベース内に格納されているプロジェクトリストを比較し、両方に
   属するものを返す
   """ 
   project_list_in_database=[i.project_name for i in DjangoProject.objects.all()]
   allproject_list=[] 
   for i in project_list:
       if i in project_list_in_database:
           allproject_list.append(i)
   return allproject_list


def start_project(project_name):
    """
    django-admin startproject projectを実行する関数
    """
    os.chdir(directory_of_projects) #current_dirをpycharmprojectsにする。
    os.mkdir(project_name) #プロジェクト名のディレクトリを作る
    os.chdir(os.path.join(directory_of_projects, project_name)) #プロジェクト名のディレクトリをcurrent_dirにする
    subprocess.Popen("django-admin startproject project", shell=True) #django-admin startproject projectを実行
    os.chdir(directory_of_projects) #current_dirをpycharmprojectsに戻す（これをしないとプログラム実行中にこのフォルダを消したりできない。）


def write_djangoruler2_in_settings_py(project_name):
    settings_py_dir=os.path.join(directory_of_projects, project_name, "project", "project", "settings.py")
    with open(settings_py_dir, "r") as f:
            sentence_list=f.readlines()
            sentence_list.insert(0, "made_by_djangoruler2_app\n")
    with open(settings_py_dir, 'w') as f:
            f.writelines(sentence_list)



#****************************************************************************************************
#***************ここからview関数**********************************************************************
#****************************************************************************************************

def main(request):
   project_list=get_project_list() 
   allproject_list=get_project_list2(project_list)
   ''' 
   初期ページで新規プロジェクトを登録するページ（実際の登録はprojectmakeで行う）
   '''
   #データベースのプロジェクトリストとフォルダ構造を調べて得られたプロジェクトリスト両方ともに属するものだけ、
   #選択可能なプロジェクトとして表示
   return render(request, "app/main.html", {"allproject_list":allproject_list})


def projectmake(request):
    #ajax
  project_list=get_project_list() 
  allproject_list=get_project_list2(project_list)
  project_name= request.POST.get("project_name")
  if not (project_name in allproject_list):      
    if re.match("^[a-zA-Z0-9_]+$", project_name): #プロジェクト名が英数文字またはアンダーバーで構成されたものかどうか
        if re.match("^[a-zA-Z]", project_name): #プロジェクト名の初期文字が大小英文字ではじまっているか
            start_project(project_name)
            settings_py_path=Path(directory_of_projects/project_name/"project"/"project"/"settings.py")
            for i in range(1000):
                 time.sleep(0.02*i) #django-admin startprojectコマンドを実行したときに、settings.pyなどのファイルができる時間差があるので、その時間を設ける
                 if settings_py_path.exists():
                        write_djangoruler2_in_settings_py(project_name)
                        break
            project=DjangoProject.objects.create(project_name=project_name)
            return HttpResponse(project_name)
        else:
            return HttpResponse("プロジェクト名の始文字はアルファベットにする。プロジェクトを新しく作るか選びなおすボタンをおしてください。")
    else:
        return HttpResponse("エラー。プロジェクト名は英数字_のみ。プロジェクトを新しく作るか選びなおすボタンをおしてください。")
  else:
       return HttpResponse("エラー。既にその名前のプロジェクトは存在します。別の名前にしてください")

def projectselect(request):
    #ajax
    project_name= request.POST.get("project_select")
    project = DjangoProject.objects.get(project_name=project_name)
    d={"project_name": project_name,"select_or_delete":"select"}
    return JsonResponse(d)



def projectdelete(request):
    #ajax
    project_name= request.POST.get("project_select")
    project = DjangoProject.objects.get(project_name=project_name)
    project.delete()
    shutil.rmtree(Path(directory_of_projects/project_name))
    d={"project_name": project_name,"select_or_delete":"delete"}
    return JsonResponse(d)


def projectreturn(request):
    #ajax
    return redirect(reverse("app:main"))
