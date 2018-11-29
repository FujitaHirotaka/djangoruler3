from . import views
from django.views.generic import TemplateView
from ajax.views import z
from django.urls import path, re_path, include




app_name = "app"

urlpatterns = [
    path('index/', views.ImgIndexView.as_view(), name='index'),
    path('create/', views.ImgCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ImgUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ImgDeleteView.as_view(), name='delete'),
]

