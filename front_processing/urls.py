from django.urls import path
from . import views

app_name = "front_processing"

urlpatterns = [
    path('', views.index, name='index'),
]