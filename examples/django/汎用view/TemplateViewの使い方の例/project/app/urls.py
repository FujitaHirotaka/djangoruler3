from django.urls import path
from . import views
from django.views.generic import TemplateView
from . import views2

app_name='app'
urlpatterns = [
	path("index/", views.index.as_view(), {"mode":"index"}, name="index"),
	path("index2/", TemplateView.as_view(template_name='app/index.html'), {"mode":"index2"}, name="index2"),
	#ここから下は本編とは関係ない
	path("ajax/", views2.ajax, name="ajax"),
	path("ajax2/", views2.ajax2, name="ajax2"),
]
