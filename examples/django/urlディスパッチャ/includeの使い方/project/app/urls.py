from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include

d = z()
d["mode"] = "index"


childpattern=[
                path(
                    "result/",
                    TemplateView.as_view(template_name="app/index.html"),
                    d,

                ),
                path(
                    "template/",
                    TemplateView.as_view(template_name="app/index.html"),
                    d,
                
                ),
                path(
                    "form/",
                    TemplateView.as_view(template_name="app/index.html"),
                    d,

                ),
            ]




app_name = "app"
urlpatterns = [
    path(
        "index/",
        TemplateView.as_view(template_name="app/index.html"),
        d,
    ),
    path(
        "application2018/may/21th/",
        include(childpattern),
    ),
]

