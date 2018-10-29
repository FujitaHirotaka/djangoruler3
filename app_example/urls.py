from django.urls import path
from . import views

app_name = "app_example"
urlpatterns = [
    path("", views.index, name="index"),
    path("ajax_api_exampleopen", views.example_open, name="example_open"),
]
