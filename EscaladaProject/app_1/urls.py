from django.contrib import admin
from django.urls import path

from app_1.views import inicio

urlpatterns = [
    path('',inicio,name = 'Inicio'),
]
