from . import views, converters
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, register_converter

register_converter(converters.RecentAnnoDominiConverter, 'annodomini')

d=z()
d["mode"]="index"

app_name='app'
urlpatterns = [
	path("index/", TemplateView.as_view(template_name="app/index.html"), d, name="index"),
	path("index/<annodomini:value>", TemplateView.as_view(template_name="app/index.html"), d, name="index2"),	
]
