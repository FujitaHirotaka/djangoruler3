from django.urls import path
from . import views

app_name='ajax'
urlpatterns = [
	path("ajax/", views.ajax, name="ajax"),
	path("ajax2/", views.ajax2, name="ajax2"),
]
