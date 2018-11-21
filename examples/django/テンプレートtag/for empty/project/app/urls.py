from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include

d = z()
d["mode"] = "index"
d["list"]=["川東","菅野","丸","安部","エルドレッド", "野間","鈴木"]
d["list2"]=[]
app_name = "app"
urlpatterns = [
    path("index/",TemplateView.as_view(template_name="app/index.html"), d, name="index"),
]

