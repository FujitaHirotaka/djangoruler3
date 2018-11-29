from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from django.views import generic
from .models import *

d=z()
d["mode"]="index"

class IndexView(generic.ListView):
    model=Player
    template_name = 'app/index.html'
    def get_context_data(self, **kwargs):
        d = super().get_context_data(**kwargs)
        e=z()
        d.update(e)
        d["mode"]="index"  
        return d


class DetailView(generic.DetailView):
    model = Player 
    template_name = 'app/index.html'   
    def get_context_data(self, **kwargs):
        d = super().get_context_data(**kwargs)
        e=z()
        d.update(e)
        d["mode"]="detail"  
        return d   
        
  
    

