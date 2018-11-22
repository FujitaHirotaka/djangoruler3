from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include
import datetime

d = z()
d["mode"] = "index"
d["Date"]=datetime.datetime.now()



app_name = "app"
urlpatterns = [
    path("index/",TemplateView.as_view(template_name="app/index.html"), d, name="index"),
]

