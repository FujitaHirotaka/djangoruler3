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
    path(
         "index/", TemplateView.as_view(template_name="app/index.html"), d, name="index"
    ),
]