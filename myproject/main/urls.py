from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index, name='home'),
    path('about/', views.get_about, name='about')
]