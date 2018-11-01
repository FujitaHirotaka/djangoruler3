from django.urls import path
from . import views

from . import views2

app_name='app'
urlpatterns = [
	path("index/", views.index.as_view(), name="index"),
	#ここから下は本編とは関係ない
	path("ajax/", views2.ajax, name="ajax"),
	path("ajax2/", views2.ajax2, name="ajax2"),
]
