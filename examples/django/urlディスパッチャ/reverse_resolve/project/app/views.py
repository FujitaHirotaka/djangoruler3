from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse

def index3(request, value, value2, value4, mode, max_hierarchy_number, file_path_list):
    return redirect(reverse("long:index2", args=(100,800)))