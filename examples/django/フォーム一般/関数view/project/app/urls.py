from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path
from copy import deepcopy
from . import forms
d = z()
d["form"] = forms.Form
d["mode"]="index"

app_name = "app"
urlpatterns = [
    path("index/", views.tashizan, name="index"),
    path("result/", views.result, name="result"),    
]