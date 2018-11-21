from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include

d = z()
d["mode"] = "index"
d["list"]=[(1,2,0), [1,3,7], (1,5,8), (2,5,7), (6,8,2)]
d["jisho"]={"aaa":"a", "bbb":"b", "ccc":"c"}
d["jisho2"]={1:"a", 2:"b", 3:"c"}
d["jisholist"]=[{1:"a", 2:"b", 3:"c"}, {4:"d", 5:"e", "ddd":"f"}]


app_name = "app"
urlpatterns = [
    path("index/",TemplateView.as_view(template_name="app/index.html"), d, name="index"),
]

