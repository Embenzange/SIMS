from django import views
from . import views 
from django.urls import path, include

urlpatterns = [
    path('', views.frontend, name="frontend"),
    path('backend/', views.backend, name="backend"),
    path('login/', include('django.contrib.auth.urls')),
]