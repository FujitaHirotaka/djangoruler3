from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include
import datetime

d = z()
d["mode"] = "index"
d["value0"]= [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
]

d["value1"]=[
    {'title': '1984', 'author': {'name': 'George', 'age': 45}},
    {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
    {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
]

d["value2"]=[
    ('a', '42'),
    ('c', 'string'),
    ('b', 'foo'),
]

app_name = "app"
urlpatterns = [
    path("index/",TemplateView.as_view(template_name="app/index.html"), d, name="index"),
]

