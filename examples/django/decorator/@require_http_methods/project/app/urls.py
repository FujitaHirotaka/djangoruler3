from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path
from copy import deepcopy
d = z()
e=deepcopy(d)
f=deepcopy(d)
e.update({"mode":"index"})
f.update({"mode":"index2"})
app_name = "app"
urlpatterns = [
    path(
         "index/", TemplateView.as_view(template_name="app/index.html"), e, name="index"
    ),
    path(
        "index2/", views.index2,  f, name="index2"
    ),
    

]
m=2