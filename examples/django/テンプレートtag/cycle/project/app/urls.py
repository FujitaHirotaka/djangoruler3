from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include

d = z()
d["mode"] = "index"
d["list"]=list(range(10))
dict2={"variable" + str(i): "<b>variable" + str(i)+"</b>" for i in range(5)}
d.update(dict2)

app_name = "app"
urlpatterns = [
    path("index/",TemplateView.as_view(template_name="app/index.html"), d, name="index"),
]

