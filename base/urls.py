from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('biography/', views.index, name='biography'),
    path('contact/', views.index, name='contact'),
    path('projects/', views.index, name='projects'),
    path('site/', views.index, name='site'),
]