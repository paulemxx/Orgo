from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [

    path('ajoutadmin', views.ajoutadmin, name='ajoutadmin'),
    path('ajoutuser', views.ajoutuser, name='ajoutuser'),
    path('listeadmin', views.listeadmin, name='listeadmin'),
    path('listeuser', views.listeuser, name='listeuser'),
]