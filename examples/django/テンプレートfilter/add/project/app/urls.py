from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include

d = z()
d["mode"] = "index"
d["value0"]=4
d["value1"]="4"
d["value2"]="文字列"
d["value3"]=[1,2,3]
d["value4"]={1:"a", 2:"b"}
d["value5"]={3:"a", 4:"b"}

app_name = "app"
urlpatterns = [
    path("index/",TemplateView.as_view(template_name="app/index.html"), d, name="index"),
]

