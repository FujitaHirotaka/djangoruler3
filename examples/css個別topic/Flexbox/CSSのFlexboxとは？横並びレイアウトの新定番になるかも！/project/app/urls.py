from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include



app_name = "app"
urlpatterns = [
    path("index/",views.index, name="index"),
]

