from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include

d = z()
d["mode"] = "index"
d["list"]=([[1,2,3], [4,5,6], [7,8,9]],[[10,11,12], [14,15,16], [17,18,19]],[[20,21,22], [24,25,26], [27,28,29]])


app_name = "app"
urlpatterns = [
    path("index/",TemplateView.as_view(template_name="app/index.html"), d, name="index"),
]

