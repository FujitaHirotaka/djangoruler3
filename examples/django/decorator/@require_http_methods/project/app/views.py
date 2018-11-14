from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST", ])
def index2(request, file_path_list, max_hierarchy_number, mode):
    d = {
        "file_path_list": file_path_list,
        "max_hierarchy_number": max_hierarchy_number,
        "mode": mode,
    }
    return render(request, "app/index.html",d)

