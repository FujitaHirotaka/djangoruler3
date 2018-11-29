from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include




app_name = "app"
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('detail/(<str:name>)/', views.DetailView.as_view(), name='detail'),#slugでは漢字が無理、pthconverterはstrにする。
]

