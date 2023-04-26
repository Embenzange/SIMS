from django import views
from django.urls import path

urlpatterns = [
    path('', views.frontend, name="frontend"),
    path('backend/', views.backend, name="backend"),
]