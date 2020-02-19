from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('biography/', views.biography, name='biography'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('site/', views.site, name='site'),
]