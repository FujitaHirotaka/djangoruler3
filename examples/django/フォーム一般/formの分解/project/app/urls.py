from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path
from copy import deepcopy
from . import forms


app_name = "app"
urlpatterns = [
    path("index/", views.Tashizan.as_view(), name="index"),
]