from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse,reverse_lazy
from django.views import generic
from .models import Img
from .forms import ImgForm




 
 
class ImgIndexView(generic.ListView):
    model = Img
    paginate_by = 2
    def get_context_data(self, *args, **kwargs):
        d=super().get_context_data(*args, **kwargs)
        e=z()
        e["mode"]="list"
        d.update(e)
        return d
 
 
class ImgCreateView(generic.CreateView):
    model = Img
    form_class = ImgForm
    success_url = reverse_lazy("app:index")
    def get_context_data(self, *args, **kwargs):
        d=super().get_context_data(*args, **kwargs)
        e=z()
        e["mode"]="form"
        d.update(e)
        return d
 
 
class ImgUpdateView(generic.UpdateView):
    model = Img
    form_class = ImgForm
    success_url = reverse_lazy("app:index")
    def get_context_data(self, *args, **kwargs):
        d=super().get_context_data(*args, **kwargs)
        e=z()
        e["mode"]="form"
        d.update(e)
        return d
 
 
class ImgDeleteView(generic.DeleteView):
    model = Img
    success_url = reverse_lazy("app:index")
    def get_context_data(self, *args, **kwargs):
        d=super().get_context_data(*args, **kwargs)
        e=z()
        e["mode"]="delete"
        d.update(e)
        return d

