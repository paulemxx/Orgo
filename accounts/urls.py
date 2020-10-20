from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [

    path('', views.register, name='register'),
    path('', views.logins, name='login'),
    path('', views.dashboard, name='dashboard'),


    ]