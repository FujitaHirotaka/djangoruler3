from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View


def index3(request, file_path_list, max_hierarchy_number, mode, value=0):
    d = {
        "file_path_list": file_path_list,
        "max_hierarchy_number": max_hierarchy_number,
        "value": value,
        "mode": mode,
    }
    print(d)
    return render(request, "app/index.html",d)

