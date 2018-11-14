from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path

d = z()
d["mode"] = "index"

app_name = "app"
urlpatterns = [
    path(
        "index/", TemplateView.as_view(template_name="app/index.html"), d, name="index"
    ),
    re_path(
        "^index/(?P<value>20[0-2][0-9])/$",
        TemplateView.as_view(template_name="app/index.html"),
        d,
        name="index2",
    ),
    re_path("^index/page-$", views.index3, d, name="index3"),
    re_path("^index/(?:page-(?P<value>[\d]+)/)$", views.index3, d, name="index4"),
    re_path(
        "^index/(?:slug_(?P<value>[\w-]+))/$",
        TemplateView.as_view(template_name="app/index.html"),
        d,
        name="index5",
    ),
]

