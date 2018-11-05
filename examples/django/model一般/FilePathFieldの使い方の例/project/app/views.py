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
    d["form"]=Form
    d["form2"]=Form2
    d["form3"]=Form3
    d["form4"]=Form4
    d["form5"]=Form5
    return render(request, 'app/index.html', d)








