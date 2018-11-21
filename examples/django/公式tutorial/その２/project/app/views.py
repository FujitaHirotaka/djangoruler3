from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse

def index(request,max_hierarchy_number, file_path_list, mode):
    aa="""<h2>Hello.<br>
        modeは{}.<br>
        max_hierarchy_numberは{}</h2>""".format(mode, max_hierarchy_number)
    return HttpResponse(aa)