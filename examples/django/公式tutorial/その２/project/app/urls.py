from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include

d = z()
d["mode"] = "index"


app_name = "app"
urlpatterns = [
    path("index/", views.index, d, name="index"),
]

