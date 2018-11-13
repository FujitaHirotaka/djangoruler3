from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View


#この部分は本編とは関係なし
########################
d=z()    
########################




def index(request):
#この部分は本編とは関係なし
########################    
    d["mode"]="index"
########################    
    
    return render(request, 'app/index.html', d)

