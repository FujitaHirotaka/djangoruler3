from django.shortcuts import render
import os
from .forms import *
from pathlib import Path
import re
from ajax.views import z

#この部分は本編とは関係なし
########################
d=z()    
########################




def index(request):

    return render(request, 'app/index.html', d)








