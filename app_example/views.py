from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from pathlib import Path
from .forms import Form
import pprint
from .models import *
import subprocess
import time
from selenium import webdriver
import threading
import psutil
import sys

# 家と学校の環境でベースパスを使い分ける
home = Path.home()
base_path = home / "PycharmProjects" / "djangoruler3" / "project" / "examples"

# base_path内にあるフォルダー名をすべて取得する


def index(request):
    large_category_list = os.listdir(base_path)
    # フォルダー構造から大カテゴリーを収集し、データーベースに登録する
    for i in large_category_list:
        large_category, created = LargeCategory.objects.get_or_create(
            largecategoryname=i
        )
        # フォルダー構造から中カテゴリーを収集し、データーベースに登録する
        for ii in os.listdir(Path(base_path) / i):
            middle_category, created = MiddleCategory.objects.get_or_create(
                largecategory=large_category, middlecategoryname=ii
            )
            for iii in os.listdir(Path(base_path) / i / ii):
                small_category, created = SmallCategory.objects.get_or_create(
                    middlecategory=middle_category, smallcategoryname=iii
                )

    # データベースにはあるがフォルダー構造から発見されない大カテゴリーや中カテゴリーをデータベースから消去する。
    for i in LargeCategory.objects.all():
        if not (i.largecategoryname in large_category_list):
            i.delete()
        else:
            middlecategory_list = os.listdir(Path(base_path) / i.largecategoryname)
            for ii in i.middlecategory_set.all():
                if not (ii.middlecategoryname in middlecategory_list):
                    ii.delete()
                else:
                    smallcategory_list = os.listdir(
                        Path(base_path) / i.largecategoryname / ii.middlecategoryname
                    )
                    for iii in ii.smallcategory_set.all():
                        if not (iii.smallcategoryname in smallcategory_list):
                            iii.delete()

    d = {"form": Form, "large_category_list": LargeCategory.objects.all()}

    return render(request, "app_example/index.html", d)


def example_open(request):
    pid1 = request.GET.get("pid")
    example_name = request.GET.get("example_select")
    middlecategory = request.GET.get("middlecategory")
    largecategory = request.GET.get("largecategory")
    pid_list = psutil.pids()
    if pid1.isdigit():
        if int(pid1) in pid_list:  # psutil.pid_exists()はどうも変数を受け付けないらしい。なので、このような記述になった。
            subprocess.Popen("taskkill /f /T /pid " + str(pid1))
    cmd="taskkill /f /T /im chromedriver.exe"
    subprocess.Popen(cmd,shell=True)
    if largecategory!="python一般":
        example_path = base_path / largecategory / middlecategory / example_name / "project"
        example_index_path = example_path / "app" / "templates" / "app"
        os.chdir(example_path)
        process1 = subprocess.Popen("python manage.py runserver 8080", shell=True)
        os.chdir(home / "PycharmProjects" / "djangoruler3" / "project")
        cmd = "python call_selenium.py " + str(process1.pid) + " " + str(example_index_path)
        subprocess.Popen(cmd, shell=True)
    elif largecategory == "python一般":
        example_path = base_path / largecategory / middlecategory / example_name 
        os.chdir(example_path)
        process1 = subprocess.Popen("python index.py", shell=True)
        os.chdir(home / "PycharmProjects" / "djangoruler3" / "project")




    d = {
        "example_name": example_name,
        "middlecategory": middlecategory,
        "largecategory": largecategory,
        "pid": process1.pid,
    }
    return JsonResponse(d)

