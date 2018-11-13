from django.urls import path
from . import views
from django.views.generic import TemplateView
from . import views2

app_name='app'
urlpatterns = [
	path("index/", views.index.as_view(template_name="app/index.html"), name="index"),
	path("index/<int:value>/", views.index.as_view(template_name="app/index.html"), name="index2"),
	path("index/<str:value>/", views.index.as_view(template_name="app/index.html"), name="index3"),
	path("index/<slug:value>/", views.index.as_view(template_name="app/index.html"), name="index4"),
    path("index/<path:value>/", views.index.as_view(template_name="app/index.html"), name="index5"),	
	#ここから下は本編とは関係ない
	path("ajax/", views2.ajax, name="ajax"),
	path("ajax2/", views2.ajax2, name="ajax2"),
]
