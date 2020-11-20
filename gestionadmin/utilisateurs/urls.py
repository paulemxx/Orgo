from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'utilisateurs'

urlpatterns = [

    path('ajoutadmin', views.ajoutadmin, name='ajoutadmin'),
    path('ajoutuser', views.ajoutuser, name='ajoutuser'),
    path('listeadmin', views.listeadmin, name='listeadmin'),
    path('listeuser', views.listeuser, name='listeuser'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_views, name='logout_views'),
]