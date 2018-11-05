from django.urls import path
from . import views
from django.views.generic import TemplateView
from ajax.views import z

d=z()
d.update({"mode":"index5"})


app_name='app'
urlpatterns = [
	path("index/", views.index, name="index"),
	path("index2/", views.index2, name="index2"),
	path("index3/", views.index3, name="index3"),	
	path("index4/", views.index4, name="index4"),	
	path("index5/", TemplateView.as_view(template_name="app/index.html"), d, name="index5"),	
]
