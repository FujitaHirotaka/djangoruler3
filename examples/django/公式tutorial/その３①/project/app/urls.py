from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include

d = z()
d["mode"] = "index"


app_name = "app"
urlpatterns = [
    path("index/", views.index, d, name="index"),
    path("<int:team_id>/", views.detail, d, name="detail"),
    path("<int:team_id>/result/", views.result, d, name="result"),
    path("<int:team_id>/vote/", views.vote, d, name="vote"),        
]

