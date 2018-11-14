from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include

d = z()
d["mode"] = "index"

app_name = "app"
urlpatterns = [
    path(
        "index/",
        TemplateView.as_view(template_name="app/index.html"),
        d,
                            name="index",
    ),
    path(
        "index/",
        include(
            [
                path(
                    "result/<int:value4>/",
                    TemplateView.as_view(template_name="app/index.html"),
                    d,
                    name="index2",
                ),
                path(
                    "template/<int:value4>/",
                    views.index3,
                    d,
                    name="index3",
                ),
            ]
        ),
    ),
]

